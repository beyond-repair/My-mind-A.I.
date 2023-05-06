import time
import random
from uuid import uuid4
from typing import Union


class GPTAgent:
    def __init__(self, agent_id: Union[str, int], agent_type: str):
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
        # Emulate work time
        self.wait()
        self_state = str(uuid4())
        self.state = self_state

    def check_work(self) -> bool:
        successful = bool(random.getrandbits(1))
        if successful:
            self.is_available = True
            self.task = None
            self.state = None
        return successful

    def wait(self) -> None:
        if self.state:
            time.sleep(random.randint(1, 5))
        else:
            time.sleep(random.randint(5, 10))
