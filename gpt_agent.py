import os
import time
import random
from uuid import uuid4
from typing import Optional, Union


# Testability change (not a new feature):
# The 2023 sketch slept a random 5-10s (or 1-5s) and then flipped a coin.
# Those draws are unchanged. Wall-clock sleep is capped by MY_MIND_MAX_SLEEP
# (seconds). The default cap is 0 so `python main.py` and pytest finish
# immediately and repeatably. Set MY_MIND_MAX_SLEEP=10 to restore pauses
# up to the original draws (max draw is 10). No model API is called.


def sleep_cap() -> float:
    raw = os.environ.get("MY_MIND_MAX_SLEEP", "0")
    try:
        return max(0.0, float(raw))
    except ValueError:
        return 0.0


def capped_sleep(seconds: float) -> None:
    delay = min(float(seconds), sleep_cap())
    if delay > 0:
        time.sleep(delay)


def simulated_pause(low: int, high: int) -> int:
    """Draw the original sleep range, then pause only up to the cap."""
    drawn = random.randint(low, high)
    capped_sleep(drawn)
    return drawn


class GPTAgent:
    def __init__(
        self,
        agent_id: Union[str, int, None] = None,
        agent_type: Optional[str] = None,
        files=None,
        capabilities=None,
        capacity: Optional[int] = None,
    ):
        # delegate_init.py builds agents with files/capabilities/capacity.
        # The class originally required (agent_id, agent_type). Accept both
        # so the 2023 call site can run. Nothing here talks to a model.
        caps = list(capabilities or [])
        self.files = list(files or [])
        self.capabilities = caps
        self.capacity = capacity
        if agent_type is None:
            agent_type = caps[0] if caps else "simulated"
        if agent_id is None:
            agent_id = agent_type
        self.agent_id = str(agent_id) if isinstance(agent_id, int) else agent_id
        self.is_available = True
        self.task = None
        self.state = None
        self.agent_type = agent_type

    def __repr__(self):
        return f'{self.agent_type}-{self.agent_id}'

    def assign_task(self, task):
        self.task = task
        self.is_available = False
        # Emulate work time (capped; see simulated_pause).
        self.wait()
        self_state = str(uuid4())
        self.state = self_state

    def check_work(self) -> bool:
        # Coin flip. Not a model response.
        successful = bool(random.getrandbits(1))
        if successful:
            self.is_available = True
            self.task = None
            self.state = None
        return successful

    def wait(self) -> None:
        if self.state:
            simulated_pause(1, 5)
        else:
            simulated_pause(5, 10)
