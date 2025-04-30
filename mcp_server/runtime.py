from typing import Dict, List
from .core import Message, Agent

class Runtime:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.queue: List[Message] = []

    def register(self, agent: Agent):
        self.agents[agent.name] = agent

    def post(self, msg: Message):
        self.queue.append(msg)

    def step(self):
        if not self.queue:
            return
        msg = self.queue.pop(0)
        receiver = self.agents.get(msg.receiver)
        if receiver:
            receiver.receive(msg)
