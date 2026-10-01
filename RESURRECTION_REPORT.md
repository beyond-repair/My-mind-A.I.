# Resurrection Report

## Original purpose

A 2023 sketch of "My Mind A.I.": several named delegates, each holding `GPTAgent`s, handing website-bug and feature tasks around. The class names suggest a GPT-backed worker. The body of `check_work` is a coin flip (`random.getrandbits(1)`). `assign_task` only sleeps. No prompt, no HTTP client, no key, no model id.

The 2026 README marks the repo SUPERSEDED, claim 0, successor `sovereign-clean-room`, and says not to start new feature work.

## Discovered implementation

Two incompatible sketches share one directory.

1. Entry sketch (intended repair target): `main.py`, `delegate_init.py`, `delegate_class.py`, `gpt_agent.py`, `task_class.py`. Tasks have title, description, and complexity. Delegates are dicts with `name`, `agents`, and `workload_capacity`. Agents were constructed with `files`, `capabilities`, and `capacity`. Constructors disagreed with the call sites, so the process died on import.

2. Abandoned drafts:
   - `my_mind.py` + `assign_tasks.py` (round-robin of strings; this part is internally consistent) + `orchestrate_agent_tasks.py`.
   - `orchestrate_agent_tasks.py` imports `get_available_agent` and `submit_agents` from `agents.py`.
   - `agents.py` is the four lines `AutoGPT`, `HuggingfaceGPT`, `BabyAGI`, `ChatGPT`. Those names are not defined. Importing the file raises `NameError`. It is not valid as a module of agents. It does parse as Python expressions, then fails at runtime.
   - `task_delegation.py` calls `Task(line)` (needs three arguments), `exec`s `delegate_init.py`, and prints `agent.name`, which `GPTAgent` does not have. It also calls `task.mark_completed`, which does not exist (`Task.complete` does).
   - `taskqueue_class.py` calls missing `Delegate.assign_agent` and `Delegate.delegate_task`, sorts with `task < other` (no `__lt__`), and assigns `task.status` (the field is `completed`).
   - `autoGPT.py` and `chatGPT.py` are raw URL lines (`https://raw.githubusercontent.com/chatgpt-prompts/...`). They are not Python (`SyntaxError: invalid syntax` on the `https:`) and they are not clients.
   - `add_one.py` maps `x + 1` over a list. Unused by the entry path. Internally consistent.
   - Leftovers: empty `New Text Document.txt`, `3E.txt` containing `<text>`, `tasks.txt`.

`__pycache__` for several of these modules was committed, including bytecode for the broken modules. That bytecode is not a hidden implementation; it was removed from the tree.

## Current state

Local branch repairs only sketch (1) so `python main.py` imports and finishes. Sleep amounts are still drawn from the original ranges, then capped (default cap 0) so the run is short and seeded (`random.seed(0)`). Nine of ten hard-coded tasks are marked complete under that seed. One is not. The summary says so. No model output is invented.

Sketch (2) is unchanged and still does not run, except `assign_tasks.py` and `add_one.py` on their own.

## Blocking problem

No model was ever integrated. The files are incompatible drafts of a pretend delegator, not a partial AI mind that can be finished by wiring a client. Adding a real LLM client would be a new product, which this repair refuses. The README already points new work at `sovereign-clean-room`.

## Attempted recovery

- Read every source file and the README, license, security template, workflow, and tests.
- Reconciled call sites in `delegate_init.py` / `main.py` with `GPTAgent` and `Delegate` by accepting the arguments the 2023 callers already passed. Did not add scheduling, tools, or network.
- Kept the coin flip. Seeded it and capped sleep so pytest is deterministic. Documented as a testability change.
- Replaced the vacuous test with an assertion that the simulation marks a task complete and does not load `openai`.
- Did not replace the conda workflow. A local pytest workflow was drafted and then dropped, because pushing any `.github/workflows/` change is rejected without the `workflow` OAuth scope. The original workflow file is unchanged and still cannot pass (`environment.yml` is missing).
- Did not delete the second stack, URL files, or leftover text uploads.
- Did not push, open a PR, or change GitHub.

## What works

- `python main.py` on the repaired branch: exit 0, simulated completions, honest count, no stderr.
- `pytest`: `test_main.py::TestMain::test_simulation_completes_without_live_api` passed on CPython 3.11.16.
- `python test_runner.py`: the same unittest, exit 0.
- `assign_tasks.py` and `add_one.py` and `task_class.py` as small local functions/classes. They are not a product.

## What does not work

- Any claim of an AI mind, GPT, AutoGPT, ChatGPT, or Hugging Face client.
- `python my_mind.py` (import of missing names from `agents.py`).
- `python agents.py` (`NameError`).
- `python task_delegation.py` (wrong `Task` arity, then missing attributes/methods).
- `TaskQueue` (`assign_agent`, `delegate_task`, ordering, `status`).
- `python autoGPT.py` / `python chatGPT.py` (`SyntaxError`; they do not chat). Confirmed on the clean clone: `autoGPT.py` exit 1, `SyntaxError: invalid syntax`.
- GitHub Actions. The original conda workflow is unchanged and still cannot pass.
- GitHub Actions execution (not run; nothing was pushed).

## Exact remaining work

To keep this repository honest, no further product work. If a later instruction allows a push: push `finish/my-mind-runnable-sketch` and only then consider a PR into `main2`. Do not add a model, keys, `environment.yml`, or a unified agent framework. Optional non-critical cleanup (leftover uploads, deleting abandoned drafts) needs an explicit ask. New agent or VSA work belongs in `sovereign-clean-room`, not here.

## Recommended future path

Use [sovereign-clean-room](https://github.com/beyond-repair/sovereign-clean-room) for new work. Do not extend this repo into a new agent product. Leave `My-mind-A.I.` as a superseded, runnable simulation sketch.
