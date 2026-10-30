# Tests

Everything here is fictional. No real school, person or company.

- `fixtures/estante/`: a small repository for a school library system (Docker Compose, crontab, backup script, yearly import, incidents). It contains one planted trap on purpose: an e-mail password written in clear in `deploy/docker-compose.yml`. The value is fake. The tests add a `.env` file with a canary value at run time, to prove that no script and no generated document ever shows it.
- `fixtures/estante-pack-r3/`: the pack the skill produced on that repository during the third test round (30/10/2026), before the round 1 to 3 fixes. The unit tests use it as a known output.
- `cases/estante/`: a full simulated run. `verdade.md` is what the developer knows (the ground truth), `perguntas.md` the questions the skill asked, `respostas.md` the answers a second agent gave in the developer's role. To repeat the test, let one agent run the skill on `fixtures/estante/` and another answer from `verdade.md` only, then compare the pack with `verdade.md`: anything that contradicts it is an invention.
- `test_scripts.py`: unit tests for the four scripts. Run from the repository root: `python3 -m unittest discover -s skills/bastao/tests`.
