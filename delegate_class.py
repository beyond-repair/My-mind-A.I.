from typing import List, Optional

from gpt_agent import GPTAgent
from task_class import Task


class Delegate:
    def __init__(
        self,
        agents: List[GPTAgent],
        max_attempts: int = 3,
        name: Optional[str] = None,
        workload_capacity: int = 0,
    ):
        # delegate_init.py passes name and workload_capacity. The 2023
        # constructor ignored them, so Delegate(**d) crashed. Store them.
        # workload_capacity is only used to order delegates in main.py.
        self.agents = agents
        self.max_attempts = max_attempts
        self.name = name
        self.workload_capacity = workload_capacity

    def delegate(self, task: Task) -> GPTAgent:
        for i in range(self.max_attempts):
            # Assign task to available agent
            for agent in self.agents:
                if agent.is_available:
                    agent.assign_task(task)
                    return agent
            # Wait for agents to become available
            for agent in self.agents:
                agent.wait()
        raise RuntimeError(f'Failed to delegate {task.description!r}')

    def check_work(self, agent: GPTAgent) -> bool:
        return agent.check_work()
