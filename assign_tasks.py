def assign_tasks(agents, tasks):
    """
    Assigns tasks to agents in a round-robin fashion, ensuring that each agent gets an equal number of tasks.
    """
    assignments = {}
    num_tasks_per_agent = len(tasks) // len(agents) if len(tasks) > len(agents) else 1

    for i, agent in enumerate(agents):
        tasks_start_idx = i * num_tasks_per_agent
        tasks_end_idx = (i + 1) * num_tasks_per_agent

        # Assign the remaining tasks to the last agent
        if i == len(agents) - 1:
            tasks_end_idx = len(tasks)

        assignments[agent] = tasks[tasks_start_idx:tasks_end_idx]

    return assignments