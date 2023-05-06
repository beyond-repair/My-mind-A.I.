from agents import get_available_agent, submit_agents
from typing import Dict, List


def orchestrate_agent_tasks(agents: List[str], assignments: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Orchestrates the agents' tasks by submitting each task to a free agent.
    Waits for each agent to complete each of its tasks.
    Returns a dictionary of results.
    """
    results = {}
    tasks = [task for _, tasks_list in assignments.items() for task in tasks_list]
    remaining_tasks = tasks
    pending_tasks = tasks

    while pending_tasks:
        for agent in agents:
            if not pending_tasks:
                break
            if agent not in get_available_agent():
                continue
            submitted_task = submit_agents(remaining_tasks[:1], agent)[0]
            remaining_tasks = remaining_tasks[1:]
            pending_tasks = [task for task in pending_tasks if task != submitted_task]

    for agent in agents:
        results[agent] = submit_agents([], agent)

    return results