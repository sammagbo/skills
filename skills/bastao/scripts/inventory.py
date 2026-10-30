#!/usr/bin/env python3
"""Bastão step 1: inventory a repository, names only.

Usage: inventory.py <repo_path> [--out inventory.json]

Never opens a .env file. Never records a value: for an inline value whose
name suggests a secret, it keeps only its length and SHA-256, so the secret
scanner can check that the value never reaches a document.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import digest, is_secret_name  # noqa: E402

SKIP_DIRS = {".git", "node_modules", "target", "build", "dist", ".venv", "venv",
             "__pycache__", ".idea", ".gradle", "passation", "passagem"}
CRON_LINE = re.compile(r"^\s*([0-9*/,\-]+\s+){4}[0-9*/,\-A-Za-z]+\s+\S")
SPRING_CRON = re.compile(r"""cron\s*=\s*["']([^"']+)["']""")
SPRING_RATE = re.compile(r"""(fixedRate|fixedDelay)(String)?\s*=\s*["']?([^,)"']+)""")
PLACEHOLDER = re.compile(r"\$\{([\w.\-]+)(?::([^}]*))?\}")
JOB_SCRIPT = re.compile(r"(backup|import|sync|export|restore|cleanup|purge|renew)", re.I)
VAR_REF = re.compile(r"\$\{?([A-Za-z_][A-Za-z0-9_]*)")


def walk(repo: Path):
    for p in sorted(repo.rglob("*")):
        if any(part in SKIP_DIRS for part in p.relative_to(repo).parts):
            continue
        if p.is_file():
            yield p


def is_env_file(p: Path) -> bool:
    """A real .env (never opened). Examples and samples are allowed."""
    n = p.name
    if not (n == ".env" or n.startswith(".env.") or n.endswith(".env")):
        return False
    return not re.search(r"(example|sample|template|dist|defaults?)", n, re.I)


# ---------- a small YAML reader for block-style compose files ----------

def _scalar(v: str):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        return [_scalar(x) for x in v[1:-1].split(",") if x.strip()]
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        return v[1:-1]
    return v


def _strip_comment(line: str) -> str:
    out, quote = [], None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "'\"":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1].isspace()):
            break
        out.append(ch)
    return "".join(out).rstrip()


def parse_yaml(text: str):
    try:
        import yaml  # type: ignore
        return yaml.safe_load(text)
    except Exception:  # PyYAML missing or failed: fallback
        pass
    lines = []
    for raw in text.splitlines():
        line = _strip_comment(raw)
        if line.strip() and not line.strip().startswith("---"):
            lines.append((len(line) - len(line.lstrip()), line.strip()))

    def block(i, indent):
        if i >= len(lines):
            return None, i
        if lines[i][1].startswith("- "):
            out = []
            while i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("- "):
                item = lines[i][1][2:]
                if re.match(r"^[\w.\-]+:\s", item) or item.endswith(":"):
                    k, _, v = item.partition(":")
                    d = {k.strip(): _scalar(v) if v.strip() else None}
                    i += 1
                    if i < len(lines) and lines[i][0] > indent:
                        sub, i = block(i, lines[i][0])
                        if isinstance(sub, dict):
                            d.update(sub)
                    out.append(d)
                else:
                    out.append(_scalar(item))
                    i += 1
            return out, i
        out = {}
        while i < len(lines) and lines[i][0] == indent:
            k, _, v = lines[i][1].partition(":")
            i += 1
            if v.strip():
                out[k.strip()] = _scalar(v)
            elif i < len(lines) and lines[i][0] > indent:
                out[k.strip()], i = block(i, lines[i][0])
            elif i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("- "):
                out[k.strip()], i = block(i, indent)
            else:
                out[k.strip()] = None
        return out, i

    if not lines:
        return {}
    data, _ = block(0, lines[0][0])
    return data


def env_items(env):
    """(name, literal value or None) from a compose environment block."""
    if isinstance(env, dict):
        for k, v in env.items():
            yield str(k), None if v is None else str(v)
    elif isinstance(env, list):
        for item in env:
            if isinstance(item, dict):
                for k, v in item.items():
                    yield str(k), None if v is None else str(v)
            else:
                k, sep, v = str(item).partition("=")
                yield k.strip(), v if sep else None


# ---------- collectors ----------

def git(repo: Path, *args) -> str:
    try:
        return subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                              text=True, timeout=20).stdout.strip()
    except Exception:
        return ""


def readme_info(repo: Path):
    for name in ("README.md", "README.rst", "README.txt", "README"):
        p = repo / name
        if p.exists():
            text = p.read_text(encoding="utf-8", errors="replace")
            title = next((ln.lstrip("# ").strip() for ln in text.splitlines()
                          if ln.startswith("#")), "")
            paras = [b.strip() for b in re.split(r"\n\s*\n", text)
                     if b.strip() and not b.strip().startswith(("#", "!", "[", "<", "```", "|"))]
            return name, title, (paras[0][:600] if paras else "")
    return None, "", ""


def compose_files(repo: Path):
    return [p for p in walk(repo)
            if re.fullmatch(r"(docker-)?compose[\w.\-]*\.ya?ml", p.name)]


def example_vars(repo: Path):
    out = {}
    for p in walk(repo):
        n = p.name
        if re.search(r"\.env\.(example|sample|template|dist)$", n) or \
           re.fullmatch(r"[\w.\-]*\.env\.(example|sample)", n) or \
           n in ("env.example", "example.env", ".env.example"):
            names = []
            for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
                m = re.match(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=", line)
                if m:
                    names.append(m.group(1))
            out[str(p.relative_to(repo))] = names
    return out


def spring_properties(repo: Path) -> dict:
    """Non-secret keys of application*.properties, to resolve ${...} in @Scheduled."""
    props = {}
    for p in walk(repo):
        if re.fullmatch(r"application[\w\-]*\.properties", p.name) and "test" not in p.parts:
            for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
                k, sep, v = line.partition("=")
                if sep and not line.lstrip().startswith("#") and not is_secret_name(k.strip()):
                    props.setdefault(k.strip(), v.strip())
    return props


def resolve(expr: str, props: dict) -> str:
    m = PLACEHOLDER.fullmatch(expr.strip())
    if not m:
        return expr
    return props.get(m.group(1)) or (m.group(2) or "") or expr


def scheduled_jobs(repo: Path):
    jobs = []
    props = spring_properties(repo)
    for p in walk(repo):
        rel = str(p.relative_to(repo))
        if is_env_file(p) or p.suffix in (".png", ".jpg", ".jar", ".zip", ".pdf", ".class"):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if "cron" in p.name.lower() or p.parent.name in ("cron.d", "cron"):
            for no, line in enumerate(text.splitlines(), 1):
                if CRON_LINE.match(line) and not line.lstrip().startswith("#"):
                    fields = line.split()
                    jobs.append({"source": f"{rel}:{no}", "kind": "crontab",
                                 "schedule": " ".join(fields[:5]),
                                 "time": cron_time(fields[:5]),
                                 "command": command_label(" ".join(fields[5:]))})
        if p.suffix == ".timer":
            m = re.search(r"OnCalendar=(.+)", text)
            jobs.append({"source": rel, "kind": "systemd-timer",
                         "schedule": m.group(1).strip() if m else "", "time": "",
                         "command": p.stem})
        if p.suffix in (".java", ".kt") and "test" not in p.relative_to(repo).parts:
            lines = text.splitlines()
            for no, line in enumerate(lines, 1):
                if "@Scheduled" not in line:
                    continue
                window = " ".join(lines[no - 1:no + 2])
                method = method_after(lines, no)
                label = f"{p.stem}.{method}" if method else p.stem
                m = SPRING_CRON.search(window)
                if m:
                    expr = resolve(m.group(1), props)
                    jobs.append({"source": f"{rel}:{no}", "kind": "spring-scheduled",
                                 "schedule": expr, "time": spring_time(expr), "command": label})
                    continue
                r = SPRING_RATE.search(window)
                if r:
                    jobs.append({"source": f"{rel}:{no}", "kind": "spring-scheduled",
                                 "schedule": f"{r.group(1)}={resolve(r.group(3), props)} ms",
                                 "time": "", "command": label})
    return jobs


def method_after(lines, no):
    for line in lines[no:no + 4]:
        m = re.search(r"\b(?:void|public|private|protected)\s+(?:\w+\s+)*(\w+)\s*\(", line)
        if m:
            return m.group(1)
    return ""


def cron_time(f):
    if len(f) >= 2 and f[0].isdigit() and f[1].isdigit():
        return f"{int(f[1]):02d}:{int(f[0]):02d}"
    return ""


def spring_time(expr):
    f = expr.split()
    if len(f) >= 3 and f[1].isdigit() and f[2].isdigit():
        return f"{int(f[2]):02d}:{int(f[1]):02d}"
    return ""


def command_label(cmd: str) -> str:
    """The script or module name of a cron command, without arguments or values."""
    cmd = cmd.split(">>")[0].split(">")[0].strip()
    m = re.search(r"([\w.\-]+\.(?:sh|py|rb|js|php|pl))", cmd)
    if m:
        return m.group(1)
    m = re.search(r"-m\s+([\w.]+)", cmd)
    if m:
        return m.group(1)
    return cmd.split()[0] if cmd else ""


def job_scripts(repo: Path):
    return [str(p.relative_to(repo)) for p in walk(repo)
            if p.suffix in (".sh", ".py", ".ps1", ".bat", ".js", ".sql")
            and JOB_SCRIPT.search(p.stem)]


def deploy_docs(repo: Path):
    return [str(p.relative_to(repo)) for p in walk(repo)
            if p.suffix.lower() in (".md", ".txt", ".rst")
            and re.search(r"(deploy|install|operac|operat|runbook|handoff|handover|"
                          r"passation|passagem|backup|restor|incident|procedure|setup)",
                          str(p.relative_to(repo)), re.I)]


def build(repo: Path) -> dict:
    readme, title, first_para = readme_info(repo)
    inv = {
        "repo_path": str(repo), "readme": readme, "project_name": title,
        "readme_first_paragraph": first_para,
        "git": {
            "remote": git(repo, "remote", "get-url", "origin"),
            "commit": git(repo, "rev-parse", "--short", "HEAD"),
            "tag": git(repo, "describe", "--tags", "--always"),
            "authors": [ln.split("\t", 1)[-1].strip() for ln in
                        git(repo, "shortlog", "-sn", "--no-merges", "HEAD").splitlines()[:5]],
        },
        "compose_files": [], "services": [], "variables": {}, "secrets_in_clear": [],
        "inline_secret_digests": [], "env_files_present": [],
        "scheduled_jobs": scheduled_jobs(repo), "job_scripts": job_scripts(repo),
        "deploy_docs": deploy_docs(repo), "migrations": [],
    }
    for p in walk(repo):
        if is_env_file(p):
            inv["env_files_present"].append(str(p.relative_to(repo)))
        if re.search(r"(migrations?|flyway|liquibase|db/changelog)", str(p.parent), re.I) \
           and p.suffix in (".sql", ".xml", ".yaml", ".yml"):
            inv["migrations"].append(str(p.relative_to(repo)))
    for path, names in example_vars(repo).items():
        for n in names:
            inv["variables"].setdefault(n, []).append(path)
    for cf in compose_files(repo):
        rel = str(cf.relative_to(repo))
        data = parse_yaml(cf.read_text(encoding="utf-8", errors="replace")) or {}
        inv["compose_files"].append({"file": rel, "name": (data or {}).get("name", "")})
        for sname, svc in ((data or {}).get("services") or {}).items():
            svc = svc or {}
            entry = {"compose_file": rel, "name": sname,
                     "container_name": svc.get("container_name", ""),
                     "image": svc.get("image", "") or ("build" if svc.get("build") else ""),
                     "ports": [str(x) for x in (svc.get("ports") or [])],
                     "volumes": [str(x).split(":")[0] for x in (svc.get("volumes") or [])],
                     "env_names": []}
            for name, value in env_items(svc.get("environment")):
                entry["env_names"].append(name)
                inv["variables"].setdefault(name, []).append(f"{rel} ({sname})")
                if value is None:
                    continue
                for ref in VAR_REF.findall(value):
                    inv["variables"].setdefault(ref, []).append(f"{rel} ({sname}, via {name})")
                literal = VAR_REF.sub("", value).strip()
                if is_secret_name(name) and literal and not VAR_REF.search(value):
                    inv["secrets_in_clear"].append({"name": name, "where": rel})
                    inv["inline_secret_digests"].append({"name": name, **digest(value)})
                elif is_secret_name(name) and ":-" in value:
                    default = value.split(":-", 1)[1].rstrip("}")
                    if default:
                        inv["secrets_in_clear"].append({"name": name, "where": rel,
                                                        "note": "default value"})
                        inv["inline_secret_digests"].append({"name": name, **digest(default)})
            inv["services"].append(entry)
    inv["variables"] = {k: sorted(set(v)) for k, v in sorted(inv["variables"].items())}
    words = set()
    for s in inv["services"]:
        words.update([s["name"], s["container_name"] or ""])
        img = str(s["image"]).split("/")[-1].split(":")[0]
        words.add(img)
    common = {digest(w)["sha256"] for w in words if w}
    for d in inv["inline_secret_digests"]:
        d["common_word"] = d["sha256"] in common
    return inv


def summary(inv: dict) -> list[str]:
    svcs = ", ".join(s["name"] for s in inv["services"]) or "none found"
    jobs = "; ".join(f'{j["time"] or j["schedule"]} {j["command"]}' for j in inv["scheduled_jobs"])
    return [
        f'1. Project: {inv["project_name"] or "?"} ({inv["readme"] or "no README"})',
        f'2. Version: tag {inv["git"]["tag"] or "?"}, commit {inv["git"]["commit"] or "?"}',
        f'3. Code lives at: {inv["git"]["remote"] or "no git remote"}',
        f'4. Authors (git): {", ".join(inv["git"]["authors"]) or "?"}',
        f'5. Services: {svcs}',
        f'6. Scheduled jobs: {jobs or "none found"}',
        f'7. Variables: {len(inv["variables"])} names, values never read',
        f'8. Secrets in clear: {", ".join(s["name"] for s in inv["secrets_in_clear"]) or "none found"}',
        f'9. Deploy and operation docs: {", ".join(inv["deploy_docs"][:6]) or "none found"}',
        f'10. Migrations: {len(inv["migrations"])}; .env files present (not opened): '
        f'{", ".join(inv["env_files_present"]) or "none"}',
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("repo")
    ap.add_argument("--out", default="inventory.json")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    if not repo.is_dir():
        print(f"not a directory: {repo}", file=sys.stderr)
        return 2
    inv = build(repo)
    Path(a.out).write_text(json.dumps(inv, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("\n".join(summary(inv)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
