from assign_tasks import assign_tasks
from orchestrate_agent_tasks import orchestrate_agent_tasks


if __name__ == '__main__':
    tasks = [
        'Task 1',
        'Task 2',
        'Task 3',
        'Task 4',
        'Task 5',
        'Task 6',
        'Task 7',
        'Task 8',
        'Task 9',
        'Task 10',
        'Task 11',
        'Task 12',
        'Task 13',
        'Task 14',
        'Task 15',
        'Task 16',
        'Task 17',
        'Task 18',
        'Task 19',
        'Task 20',
    ]
    agents = [
        'Agent 1',
        'Agent 2',
        'Agent 3',
        'Agent 4',
        'Agent 5',
    ]

    assignments = assign_tasks(agents, tasks)
    results = orchestrate_agent_tasks(agents, assignments)

    print(results)