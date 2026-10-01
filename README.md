<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║   ATOMIC DREAM LABS  ·  BEYOND-REPAIR                        ║
╚══════════════════════════════════════════════════════════════╝
```

# My Mind A.I.

### Early agent sketch.

[![Lifecycle](https://img.shields.io/badge/●_SUPERSEDED-f59e0b?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_0-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   SUPERSEDED
SUCCESSOR   sovereign-clean-room
CLAIM       0   historical
```

</div>

---
> **SUPERSEDED:** Early agent sketch. This is not a language model and not a product.
> Canonical successor: [sovereign-clean-room](https://github.com/beyond-repair/sovereign-clean-room)
> Do not start new feature work here. Do not extend this repo into a new agent product.

## STATUS

SUPERSEDED. The runnable piece is a 2023 toy delegator that pretends to be GPT. Feature work stops here.

## What this is

A simulated multi-agent task delegator. `GPTAgent` does not call an API. It draws the original sleep range, pauses only up to a cap, then coin-flips success. Python 3.11+ and the standard library are enough. There is no package install, no config file, and no secrets.

Preserved one-line description from the upload era: **A.I.**

## Run

From the repository root:

```bash
python main.py
```

Exit code 0 means the simulation finished. Stdout lists each task, prints `<title> completed` when the coin flip succeeds, then a line of the form `Simulation finished: N/10 tasks marked complete by a coin-flip, not a language model.` Some delegates have no agents (or agents stuck after a failed flip). Those attempts print `Error: Failed to delegate ...`. That is the old sketch, not a live model failure.

`MY_MIND_MAX_SLEEP` (seconds) caps wall-clock pauses. Default is `0` so a smoke run does not sleep 5–10 seconds per attempt. The random draw is still taken. Set `MY_MIND_MAX_SLEEP=10` to restore pauses up to the original draws. `main.py` uses a fixed seed (`0`) so the coin flips repeat.

## Test

```bash
python -m pip install pytest
pytest
```

`test_main.py` imports `main` and asserts at least one task is marked complete by the simulation, and that no OpenAI client was loaded.

`python test_runner.py` runs that same unittest.

## Layout

Entry path (the one that runs):

- `main.py` builds ten `Task`s and one `Delegate` per spec in `delegate_init.py`.
- `delegate_init.py` constructs `GPTAgent`s with `files`, `capabilities`, and `capacity`, grouped into named delegates with `workload_capacity`.
- `delegate_class.py` gives a task to the first available agent. It does not match capabilities.
- `gpt_agent.py` simulates work and flips a coin in `check_work`.
- `task_class.py` stores `title`, `description`, `complexity`, and `completed`.

Abandoned incompatible drafts (not the entry point, not finished):

- `my_mind.py` round-robins string tasks via `assign_tasks.py`, then calls `orchestrate_agent_tasks.py`.
- `orchestrate_agent_tasks.py` imports `get_available_agent` and `submit_agents` from `agents.py`. Those functions do not exist.
- `agents.py` is four bare product names (`AutoGPT`, `HuggingfaceGPT`, `BabyAGI`, `ChatGPT`). It is not an agent module. Executing it raises `NameError`.
- `task_delegation.py` builds `Task` with one argument (the class needs three), `exec`s `delegate_init.py`, and expects `agent.name`.
- `taskqueue_class.py` calls `Delegate.assign_agent` / `delegate_task` (not defined), compares `Task` with `<` (not defined), and sets `task.status` (the field is `completed`).
- `autoGPT.py` and `chatGPT.py` are raw GitHub URLs saved as `.py` files. They are not valid Python (`SyntaxError`) and they are not clients.
- `add_one.py` is a tiny unrelated helper and is internally consistent. Nothing in the entry path uses it.

Leftover uploads, kept on purpose: `New Text Document.txt` (empty), `3E.txt` (`<text>`), `tasks.txt`.

## CI

`.github/workflows/python-package-conda.yml` is still the workflow on the branch, and it cannot pass. It runs `conda env update --file environment.yml`, but `environment.yml` was never committed, and `actions/setup-python` does not set `$CONDA`. It was left in place because this GitHub login cannot create or update Actions workflow files (the token has no `workflow` scope). Run pytest locally instead. Details are in `COMPLETION_REPORT.md`.

## License

MIT. See `LICENSE`.
