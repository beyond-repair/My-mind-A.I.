from typing import List

from delegate_class import Delegate
from gpt_agent import GPTAgent

def create_delegates_and_agents() -> List[dict]:
    agents = [
        GPTAgent(files=['web_app.py'], capabilities=['fix_web_app_bug'], capacity=3),
        GPTAgent(files=['web_app.py'], capabilities=['fix_api_bug'], capacity=5),
        GPTAgent(files=['web_app.py'], capabilities=['create_admin_ui'], capacity=2),
        GPTAgent(files=['web_app.py'], capabilities=['create_invoice_ui'], capacity=2),
        GPTAgent(files=['web_app.py'], capabilities=['implement_feature_x'], capacity=10),
        GPTAgent(files=['web_app.py'], capabilities=['refactor_database'], capacity=3),
        GPTAgent(files=['web_app.py'], capabilities=['implement_feature_y'], capacity=7),
        GPTAgent(files=['web_app.py'], capabilities=['test_code'], capacity=8),
    ]
    delegates = [
        {
            'name': 'Bugs delegate',
            'agents': agents[:2],
            'workload_capacity': 10,
        },
        {
            'name': 'UI delegate',
            'agents': agents[2:4],
            'workload_capacity': 7,
        },
        {
            'name': 'Feature implementation delegate',
            'agents': agents[4:6],
            'workload_capacity': 18,
        },
        {
            'name': 'Testing delegate',
            'agents': agents[6:8],
            'workload_capacity': 15,
        },
        {
            'name': 'Maintenance delegate',
            'agents': agents[8:],
            'workload_capacity': 30,
        },
    ]
    return delegates


agents = create_delegates_and_agents()