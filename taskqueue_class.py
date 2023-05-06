from typing import List
from task_class import Task
from delegate_class import Delegate
from gpt_agent import GPTAgent

class TaskQueue:
    def __init__(self, tasks: List[Task], delegate: Delegate):
        self.tasks = tasks
        self.delegate = delegate

    def add_task(self, task: Task) -> None:
        if not self.tasks:
            self.tasks.append(task)
        else:
            for i in range(len(self.tasks)):
                if task < self.tasks[i]:
                    self.tasks.insert(i, task)
                    return None
            self.tasks.append(task)

    def next_task(self, agent: GPTAgent) -> Task:
        for task in self.tasks:
            appropriate_agent = self.delegate.assign_agent(task)
            if appropriate_agent == agent:
                self.delegate.delegate_task(task, agent)
                self.tasks.remove(task)
                return task

        return None

    def complete_task(self, task: Task) -> None:
        task.status = 'completed'
