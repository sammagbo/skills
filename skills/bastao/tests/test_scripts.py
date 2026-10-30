"""Tests for the four Bastão scripts, on the fictional Estante fixture.

Run from the repository root: python3 -m unittest discover -s skills/bastao/tests
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent / "scripts"
FIXTURE = HERE / "fixtures" / "estante"
PACK = HERE / "fixtures" / "estante-pack-r3"
CANARY = "CANARY-ENV-7f3a9"


def run(script: str, *args) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)],
                          capture_output=True, text=True)


class EstanteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        cls.repo = cls.tmp / "estante"
        shutil.copytree(FIXTURE, cls.repo)
        # A real .env with a canary value: the scripts must never print it.
        (cls.repo / "deploy" / ".env").write_text(f"POSTGRES_PASSWORD={CANARY}\n", encoding="utf-8")
        subprocess.run(["git", "init", "-q"], cwd=cls.repo, check=True)
        subprocess.run(["git", "add", "-A", ".", ":!deploy/.env"], cwd=cls.repo, check=True)
        subprocess.run(["git", "-c", "user.email=dev@example.org", "-c", "user.name=Dev Ficticio",
                        "commit", "-qm", "fixture"], cwd=cls.repo, check=True)
        cls.inv_path = cls.tmp / "inventory.json"
        cls.inv_run = run("inventory.py", cls.repo, "--out", cls.inv_path)
        cls.inv = json.loads(cls.inv_path.read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    # inventory.py
    def test_inventory_finds_services_jobs_and_secret_in_clear(self):
        self.assertEqual(self.inv_run.returncode, 0)
        self.assertEqual([s["name"] for s in self.inv["services"]], ["db", "app", "caddy"])
        self.assertEqual([(j["time"], j["command"]) for j in self.inv["scheduled_jobs"]],
                         [("02:30", "backup.sh"), ("07:00", "app.lembretes")])
        self.assertEqual([s["name"] for s in self.inv["secrets_in_clear"]], ["SMTP_PASSWORD"])
        self.assertEqual(self.inv["git"]["authors"], ["Dev Ficticio"])
        self.assertIn("deploy/.env", self.inv["env_files_present"])

    def test_inventory_never_records_values(self):
        text = self.inv_path.read_text(encoding="utf-8") + self.inv_run.stdout
        self.assertNotIn(CANARY, text)
        self.assertNotIn("Tq8vR2mLx9pZ4kWc", text)  # the inline SMTP password of the fixture

    # secret_scanner.py
    def test_scanner_passes_the_generated_pack(self):
        r = run("secret_scanner.py", PACK, "--inventory", self.inv_path, "--repo", self.repo)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_scanner_catches_planted_secrets_without_printing_them(self):
        bad = self.tmp / "bad"
        bad.mkdir()
        (bad / "05-x.md").write_text(
            "SMTP_PASSWORD=Tq8vR2mLx9pZ4kWc\n"
            "postgres://estante:hunter2xyz@db:5432/estante\n"
            f"Le mot de passe est {CANARY}.\n"
            "ADMIN_PIN: 4821\n"
            "| SMTP_PASSWORD | mot de passe du courriel | deploy/docker-compose.yml |\n",
            encoding="utf-8")
        r = run("secret_scanner.py", bad, "--inventory", self.inv_path, "--repo", self.repo)
        self.assertEqual(r.returncode, 1)
        for rule in ("1 assignment", "2 credential URL", "6 inline value of SMTP_PASSWORD",
                     "7 .env value of POSTGRES_PASSWORD"):
            self.assertIn(rule, r.stdout)
        self.assertNotIn("05-x.md:5", r.stdout)  # a name in a table is allowed
        self.assertNotIn(CANARY, r.stdout)
        self.assertNotIn("Tq8vR2mLx9pZ4kWc", r.stdout)

    # coverage_check.py
    def test_coverage_reports_counts_and_known_gaps(self):
        r = run("coverage_check.py", self.inv_path, PACK / "passation", "--pair", PACK / "passagem")
        self.assertIn("| 05-garde-des-acces.md |", r.stdout)
        self.assertIn("service caddy", r.stdout)  # round 3 did not name the services
        self.assertNotIn("not explained", r.stdout)
        self.assertNotIn("scheduled job", r.stdout)
        self.assertNotIn("parity", r.stdout)

    def test_coverage_requires_secret_in_clear_in_document_6(self):
        pack = self.tmp / "pack"
        shutil.copytree(PACK / "passagem", pack)
        doc6 = pack / "06-checklist-de-recepcao.md"
        doc6.write_text(doc6.read_text(encoding="utf-8").replace("SMTP_PASSWORD", "senha"),
                        encoding="utf-8")
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertIn("secret in clear SMTP_PASSWORD is not an open point", r.stdout)

    # style_check.py
    def test_style_passes_the_generated_pack(self):
        for lang in ("passation", "passagem"):
            r = run("style_check.py", PACK / lang)
            self.assertEqual(r.returncode, 0, r.stdout)

    def test_style_flags_machine_writing(self):
        pt = self.tmp / "passagem"
        pt.mkdir()
        (pt / "01-o-que-e.md").write_text(
            "# Estante: o que é\n## O Que Ele Faz Na Escola\n"
            "- **Verificação:** vale ressaltar que o sistema é robusto — e “seguro”.\n"
            "Não só registra, mas também envia.\n"
            "`comando — com travessão` não conta.\n", encoding="utf-8")
        r = run("style_check.py", pt)
        self.assertEqual(r.returncode, 1)
        for rule in ("rule 1", "rule 2", "rule 3", "rule 4", "rule 7", "rule 9"):
            self.assertIn(rule, r.stdout)
        self.assertNotIn(":5 ", r.stdout)


if __name__ == "__main__":
    unittest.main()
