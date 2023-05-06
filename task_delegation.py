from typing import List

from delegate_class import Delegate
from task_class import Task
from gpt_agent import GPTAgent


def main() -> None:
    tasks_file = 'tasks.txt'
    delegate_init_file = 'delegate_init.py'

    # Initialize tasks
    tasks = []
    with open(tasks_file) as f:
        lines = f.readlines()
        for line in lines:
            tasks.append(Task(line.strip()))

    # Initialize delegate
    exec(open(delegate_init_file).read())
    delegate = Delegate(agents)

    # Delegate tasks
    for task in tasks:
        # Assign task to an agent
        agent = delegate.delegate(task)
        # Wait for agent to complete task
        while not delegate.check_work(agent):
            # If agent failed the task, reassign the task
            agent = delegate.delegate(task)

        task.mark_completed()
        print(f'Marked {task.description!r} as completed by {agent.name!r} ({agent})')


if __name__ == '__main__':
    main()
