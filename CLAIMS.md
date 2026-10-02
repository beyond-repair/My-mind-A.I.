# Claims

**Repository:** `beyond-repair/My-mind-A.I.`
**Branch:** `main2`
**Head at Sweep-201 discovery:** `b886113ac490560f8b746a24fbda0c494b3b9433`
**Classification:** SUPERSEDED
**Successor:** `sovereign-clean-room`
**Claim level:** 0 (historical sketch)

## Allowed statements

- This tree contains a 2023 multi-agent task sketch.
- `GPTAgent` does not call an API. Completion is a seeded coin flip in `gpt_agent.py`.
- `python -m unittest test_main.py` passed locally in Sweep-201 (1 test, seed 0, `MY_MIND_MAX_SLEEP` default 0). That is a simulation check, not a model evaluation.
- Default branch is `main2`, not `main`.

## Forbidden statements

- This is not a language model, product agent, or successor to AutoGPT / ChatGPT / BabyAGI.
- `autoGPT.py` and `chatGPT.py` are URL stubs, not clients.
- `agents.py` is not an importable agent module.
- CI is not green. `.github/workflows/python-package-conda.yml` still fails (latest run 36851325554, conclusion failure) because `environment.yml` is absent and `$CONDA` is unset. Workflow files were not edited this cycle.

## Operator-only

- GitHub archive flag. Still `archived=false`.
- Replace or disable the conda workflow. Requires a token with `workflow` scope.
