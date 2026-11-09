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
PACK = HERE / "fixtures" / "estante-pack"
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

    def test_inventory_skips_the_pack_but_not_its_folder(self):
        repo = self.tmp / "repo-with-pack"
        shutil.copytree(self.repo, repo)
        # A French pack written into docs/, beside the repository's own documents,
        # its Portuguese twin in handover-pt/, and an old handover to leave out.
        for name in ("04-si-ca-casse.md", "00-questions.md", "proposition-04-si-ca-casse.md",
                     "answers.yml", "verification.md"):
            (repo / "docs" / name).write_text("# x\n", encoding="utf-8")
        (repo / "handover-pt").mkdir()
        (repo / "handover-pt" / "04-se-quebrar.md").write_text("# x\n", encoding="utf-8")
        (repo / "docs" / "old").mkdir()
        (repo / "docs" / "old" / "runbook.md").write_text("# x\n", encoding="utf-8")
        out = repo / "docs" / "inventory.json"
        self.assertEqual(run("inventory.py", repo, "--out", out, "--skip", "docs/old").returncode, 0)
        inv = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(inv["deploy_docs"], ["docs/deploy.md", "docs/incidentes.md"])
        self.assertEqual([s["name"] for s in inv["services"]], ["db", "app", "caddy"])

    def test_inventory_creates_the_pack_folder(self):
        out = self.tmp / "not-yet" / "passagem" / "inventory.json"
        self.assertEqual(run("inventory.py", self.repo, "--out", out).returncode, 0)
        self.assertTrue(out.is_file())

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

    def test_scanner_accepts_a_lowercase_setting_but_not_a_mixed_case_token(self):
        ok = self.tmp / "settings"
        ok.mkdir()
        (ok / "03-rotina.md").write_text("# t\n\nAbrir com charset=utf-8 no fim. Ou encoding=utf-8.\n", encoding="utf-8")
        r = run("secret_scanner.py", ok, "--inventory", self.inv_path, "--repo", self.repo)
        self.assertEqual(r.returncode, 0, r.stdout)
        bad = self.tmp / "settings-bad"
        bad.mkdir()
        (bad / "03-rotina.md").write_text("# t\n\nUse x=aB3dE9fG2hJkL1 para entrar.\n", encoding="utf-8")
        r = run("secret_scanner.py", bad, "--inventory", self.inv_path, "--repo", self.repo)
        self.assertEqual(r.returncode, 1, r.stdout)

    # coverage_check.py
    def test_coverage_passes_the_generated_pack(self):
        r = run("coverage_check.py", self.inv_path, PACK / "passagem", "--pair", PACK / "passation")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("| 05-custodia-de-acessos.md |", r.stdout)
        self.assertIn("| 05-garde-des-acces.md |", r.stdout)
        self.assertIn("0 problem(s), 0 warning(s)", r.stdout)

    def test_coverage_names_a_service_missing_from_document_1(self):
        pack = self.tmp / "no-caddy"
        shutil.copytree(PACK / "passagem", pack)
        doc1 = pack / "01-o-que-e.md"
        doc1.write_text(doc1.read_text(encoding="utf-8").replace("estante-caddy", "o cadeado"), encoding="utf-8")
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertIn("service caddy", r.stdout)

    def test_the_fixture_fingerprints_match_its_documents(self):
        import hashlib
        text = (PACK / "passagem" / "verification.md").read_text(encoding="utf-8")
        rows = [ln for ln in text.splitlines() if ln.startswith("| passag") or ln.startswith("| passat")]
        self.assertEqual(len(rows), 12)
        for ln in rows:
            _, name, digest, _ = [c.strip() for c in ln.split("|")]
            self.assertEqual(hashlib.sha256((PACK / name).read_bytes()).hexdigest(), digest, name)

    def test_coverage_requires_secret_in_clear_in_document_6(self):
        pack = self.tmp / "pack"
        shutil.copytree(PACK / "passagem", pack)
        doc6 = pack / "06-checklist-de-recepcao.md"
        doc6.write_text(doc6.read_text(encoding="utf-8").replace("SMTP_PASSWORD", "senha"),
                        encoding="utf-8")
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertIn("secret in clear SMTP_PASSWORD is not an open point", r.stdout)

    def test_coverage_accepts_a_draft_document_4_that_points_to_the_questions_file(self):
        pack = self.tmp / "draft"
        shutil.copytree(PACK / "passagem", pack)
        doc4 = pack / "04-se-quebrar.md"
        text = doc4.read_text(encoding="utf-8")
        start = text.index("## Os lembretes por e-mail não saem")
        end = text.index("Outros sintomas:")
        without_third = text[:start] + text[end:]            # two symptoms and the pointer line
        pointer = "Outros sintomas: pergunta 16 de 00-perguntas.md.\n"
        doc4.write_text(without_third, encoding="utf-8")
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertNotIn("3 or 4 expected", r.stdout)
        self.assertIn("WARNING 04-se-quebrar.md: 2 symptom(s), the others wait in the questions file", r.stdout)
        doc4.write_text(without_third.replace(pointer, ""), encoding="utf-8")   # no pointer: a failure
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertIn("04-se-quebrar.md: 2 symptom(s), 3 or 4 expected", r.stdout)
        doc4.write_text(without_third, encoding="utf-8")
        (pack / "00-perguntas.md").unlink()                                     # pointer to a missing file
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertIn("04-se-quebrar.md: names 00-perguntas.md, which is not in the pack", r.stdout)

    def test_scripts_skip_the_questions_file_and_read_proposals(self):
        pack = self.tmp / "with-proposal"
        shutil.copytree(PACK / "passagem", pack)
        bad = "# Estante: o que é\n\nVale ressaltar que o sistema é robusto — e “seguro”.\n"
        long_step = ("# Estante: se quebrar\n\n- Verifique se a luz verde da câmera da entrada está acesa e se o cabo "
                     "de rede está encaixado atrás do aparelho antes de chamar alguém.\n")
        (pack / "00-perguntas.md").write_text(bad, encoding="utf-8")
        (pack / "01-o-que-e.proposta.md").write_text(bad, encoding="utf-8")  # not a proposal: wrong name
        (pack / "proposta-04-se-quebrar.md").write_text(long_step, encoding="utf-8")
        # style_check reads the proposal as document 4, in Portuguese, and skips the questions file.
        r = run("style_check.py", pack, "--max-sentences", "99")
        self.assertIn("proposta-04-se-quebrar.md:3  rule 21  sentence of 26 words, limit 20", r.stdout)
        self.assertNotIn("00-perguntas", r.stdout)
        self.assertNotIn("01-o-que-e.proposta", r.stdout)
        # coverage_check checks the documents; with --merged the proposal stands in for document 4.
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertIn("| 04-se-quebrar.md |", r.stdout)
        self.assertNotIn("proposta", r.stdout)
        r = run("coverage_check.py", self.inv_path, pack, "--merged")
        self.assertIn("| proposta-04-se-quebrar.md |", r.stdout)
        self.assertNotIn("| 04-se-quebrar.md |", r.stdout)

    # style_check.py
    def test_style_passes_the_generated_pack(self):
        for lang in ("passation", "passagem"):
            r = run("style_check.py", PACK / lang)
            self.assertEqual(r.returncode, 0, r.stdout)

    def test_style_passes_the_templates(self):
        for lang in ("fr", "pt"):
            r = run("style_check.py", HERE.parent / "templates" / lang)
            self.assertEqual(r.returncode, 0, r.stdout)

    def test_style_flags_sentence_and_paragraph_limits(self):
        pt = self.tmp / "ste"
        pt.mkdir()
        long_step = "Verifique se a luz verde da câmera da entrada está acesa e se o cabo de rede está " \
                    "encaixado atrás do aparelho antes de chamar alguém.\n"  # 26 words
        (pt / "04-se-quebrar.md").write_text("# Estante: se quebrar\n\n- " + long_step, encoding="utf-8")
        (pt / "01-o-que-e.md").write_text(
            "# Estante: o que é\n\n" + "O sistema registra quem entra. " * 7 + "\n", encoding="utf-8")
        r = run("style_check.py", pt)
        self.assertEqual(r.returncode, 1)
        self.assertIn("04-se-quebrar.md:3  rule 21  sentence of 26 words, limit 20", r.stdout)
        self.assertIn("01-o-que-e.md:3  rule 22  paragraph of 7 sentences, limit 3", r.stdout)
        r = run("style_check.py", pt, "--max-words", "35")
        self.assertNotIn("rule 21", r.stdout)
        self.assertIn("rule 22", r.stdout)
        r = run("style_check.py", pt, "--max-sentences", "7")
        self.assertNotIn("rule 22", r.stdout)

    def test_style_flags_jargon_in_the_plain_documents_only(self):
        d = self.tmp / "jargon"
        d.mkdir()
        text = "# Estante: texto\n\nMude o IP da impressora no roteador. Use UTF-8 e o repositório.\n"
        for name in ("01-o-que-e.md", "04-se-quebrar.md", "06-checklist-de-recepcao.md",
                     "02-quem-faz-o-que.md", "03-rotina.md", "05-custodia-de-acessos.md"):
            (d / name).write_text(text, encoding="utf-8")
        r = run("style_check.py", d)
        for name in ("01-o-que-e.md", "04-se-quebrar.md", "06-checklist-de-recepcao.md"):
            self.assertIn(f'{name}:3  rule 31  technical term "IP", use the plain expression', r.stdout)
            self.assertIn(f'{name}:3  rule 31  technical term "roteador", use the plain expression', r.stdout)
            self.assertIn(f'{name}:3  rule 31  technical term "UTF-8", use the plain expression', r.stdout)
        for name in ("02-quem-faz-o-que.md", "03-rotina.md", "05-custodia-de-acessos.md"):
            self.assertNotIn(name, r.stdout)

    def test_scripts_say_clearly_when_a_folder_is_missing(self):
        for script, args in (("style_check.py", ["nope-folder"]),
                             ("secret_scanner.py", ["nope-folder"]),
                             ("coverage_check.py", [self.inv_path, "nope-folder"])):
            r = run(script, *args)
            self.assertEqual(r.returncode, 2, script)
            self.assertNotIn("Traceback", r.stderr, script)
            self.assertIn("give an absolute path", r.stderr, script)

    def test_style_reads_blocks_not_lines(self):
        d = self.tmp / "blocks"
        d.mkdir()
        # French: an abbreviation is not a sentence end; three sentences pass.
        (d / "01-ce-que-cest.md").write_text(
            "# Estante : ce que c'est\n\n"
            "Le programme note qui entre. Le programme note qui sort. M. Silva ouvre le portail.\n",
            encoding="utf-8")
        # Portuguese, document 2: same with "Sr."; a paragraph wrapped over three lines is two sentences.
        (d / "02-quem-faz-o-que.md").write_text(
            "# Estante: quem faz o quê\n\n"
            "O sistema registra quem entra. O Sr. Silva abre o portão. O Dr. Costa assina.\n\n"
            "O sistema registra quem entra e\nquem sai pelo portão e pela\ncantina todos os dias.\n"
            "Ele não tranca nenhuma porta.\n", encoding="utf-8")
        # Document 3: a URL and an e-mail are one word each; a sentence wrapped over two lines is read whole.
        (d / "03-rotina.md").write_text(
            "# Estante: rotina\n\n"
            "- Abrir https://estante.escola.exemplo.br/admin/relatorios/entradas/hoje e escrever para "
            "suporte@escola.exemplo.br se a tela ficar branca.\n\n"
            "Verificar se a luz verde da câmera da entrada está acesa e se o cabo de rede\n"
            "está encaixado atrás do aparelho antes de chamar alguém.\n\n"
            "- Um. Dois. Três. Quatro. Cinco. Seis. Sete.\n", encoding="utf-8")
        # Document 4, French: « Erreur ! » ends no sentence; a wrapped line that starts with
        # inline code starts a new sentence; "1)" items and an empty quote line end a block.
        (d / "04-si-ca-casse.md").write_text(
            "# Estante : si ça casse\n\n"
            "Le site affiche « Erreur ! » quand on ouvre la page. Appelez Denise. Notez l'heure.\n\n"
            "- Vérifier sur la machine de la salle des serveurs que le programme tourne.\n"
            "  `docker compose ps` doit montrer les trois boîtes du programme avec le mot Up.\n\n"
            "1) Ouvrir l'écran.\n2) Cliquer sur Prêts.\n3) Vérifier la date.\n4) Noter le résultat.\n\n"
            "> Une phrase. Deux phrases.\n>\n> Trois phrases. Quatre phrases.\n", encoding="utf-8")
        # Document 5: outside documents 3 and 4, a list item keeps to three sentences.
        (d / "05-custodia-de-acessos.md").write_text(
            "# Estante: custódia de acessos\n\n- Um. Dois. Três. Quatro.\n", encoding="utf-8")
        r = run("style_check.py", d)
        self.assertNotIn("01-ce-que-cest.md", r.stdout)
        self.assertNotIn("02-quem-faz-o-que.md", r.stdout)
        self.assertNotIn("04-si-ca-casse.md", r.stdout)
        self.assertNotIn("03-rotina.md:3 ", r.stdout)
        self.assertIn("03-rotina.md:5  rule 21  sentence of 26 words, limit 20", r.stdout)
        self.assertIn("03-rotina.md:8  rule 22  list item of 7 sentences, limit 6", r.stdout)
        self.assertIn("05-custodia-de-acessos.md:3  rule 22  list item of 4 sentences, limit 3", r.stdout)
        self.assertIn("3 flag(s)", r.stdout)

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
