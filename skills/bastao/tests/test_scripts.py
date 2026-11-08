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

    def test_coverage_accepts_a_draft_document_4_that_points_to_the_questions_file(self):
        pack = self.tmp / "draft"
        shutil.copytree(PACK / "passagem", pack)
        doc4 = pack / "04-se-quebrar.md"
        text = doc4.read_text(encoding="utf-8")
        start = text.index("## A impressora não imprime mais")
        end = text.index("## As famílias não recebem mais os lembretes")
        doc4.write_text(text[:start] + text[end:], encoding="utf-8")  # two symptoms left
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertIn("04-se-quebrar.md: 2 symptom(s), 3 or 4 expected", r.stdout)
        doc4.write_text(text[:start] + "Outros sintomas: pergunta 5 de 00-perguntas.md.\n\n" + text[end:],
                        encoding="utf-8")
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertIn("04-se-quebrar.md: names 00-perguntas.md, which is not in the pack", r.stdout)
        (pack / "00-perguntas.md").write_text("# Perguntas\n", encoding="utf-8")
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertNotIn("3 or 4 expected", r.stdout)
        self.assertNotIn("not in the pack", r.stdout)
        self.assertIn("WARNING 04-se-quebrar.md: 2 symptom(s), the others wait in the questions file", r.stdout)

    def test_scripts_skip_the_questions_file_and_proposals(self):
        pack = self.tmp / "with-proposal"
        shutil.copytree(PACK / "passagem", pack)
        bad = "# Estante: o que é\n\nVale ressaltar que o sistema é robusto — e “seguro”.\n"
        for name in ("00-perguntas.md", "proposta-01-o-que-e.md", "01-o-que-e.proposta.md"):
            (pack / name).write_text(bad, encoding="utf-8")
        r = run("style_check.py", pack, "--max-words", "35", "--max-sentences", "99")
        self.assertEqual(r.returncode, 0, r.stdout)
        r = run("coverage_check.py", self.inv_path, pack)
        self.assertIn("| 01-o-que-e.md |", r.stdout)
        self.assertNotIn("proposta", r.stdout)

    # style_check.py
    def test_style_passes_the_generated_pack(self):
        # The round 3 pack predates rules 21 and 22 (ASD-STE100): it is checked
        # with the limits of its time (35 words, no paragraph limit) until it is regenerated.
        for lang in ("passation", "passagem"):
            r = run("style_check.py", PACK / lang, "--max-words", "35", "--max-sentences", "99")
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
