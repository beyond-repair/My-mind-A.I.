import time

from delegate_init import agents
from delegate_class import Delegate
from task_class import Task


def main():

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

    # Task complete
    print('All tasks completed')
    time.sleep(2)
    print('Shutting down')


if __name__ == '__main__':
    main()
