import random

from delegate_init import agents
from delegate_class import Delegate
from gpt_agent import capped_sleep
from task_class import Task


# Fixed seed so the coin-flip sketch is repeatable. Not a model.
SIMULATION_SEED = 0


def main():
    random.seed(SIMULATION_SEED)

    # Initialize tasks
    tasks = [
        Task('Fix authentication bug', 'Fix a bug in the login system', 2),
        Task('Create admin panel', 'Allow admins to easily manage user accounts', 4),
        Task('Implement feature X', 'Add feature X to the website', 6),
        Task('Refactor database schema', 'Improve the database schema design', 3),
        Task('Test user registration workflow', 'Ensure that new users can register without issues', 1),
        Task('Implement feature Y', 'Add feature Y to the website', 5),
        Task('Redesign user profile page', 'Improve the design of user profile pages', 4),
        Task('Test search functionality', 'Ensure that search results are relevant and sorted', 2),
        Task('Create API endpoint for mobile app', 'Allow the mobile app to fetch data from the server', 3),
        Task('Implement feature Z', 'Add feature Z to the website', 7),
    ]

    # Initialize delegates
    delegates = [Delegate(**d) for d in agents]

    # Iterate over tasks
    for task in tasks:
        print(f'Task: {task.title} (complexity {task.complexity}, description: {task.description})')
        delegates.sort(key=lambda d: d.workload_capacity)
        for delegate in delegates:
            try:
                agent = delegate.delegate(task)
                successful = delegate.check_work(agent)
                if successful:
                    task.complete()
                    break
            except Exception as e:
                print(f'Error: {e}')

    done = sum(1 for task in tasks if task.completed)
    print(
        f'Simulation finished: {done}/{len(tasks)} tasks marked complete '
        f'by a coin-flip, not a language model.'
    )
    # Original sketch paused 2 seconds here. Same cap as agent sleeps.
    capped_sleep(2)
    print('Shutting down')
    return tasks


if __name__ == '__main__':
    main()
