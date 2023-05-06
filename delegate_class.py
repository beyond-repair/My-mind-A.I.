from typing import List

from gpt_agent import GPTAgent
from task_class import Task


class Delegate:
    def __init__(self, agents: List[GPTAgent], max_attempts: int = 3):
        self.agents = agents
        self.max_attempts = max_attempts

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
