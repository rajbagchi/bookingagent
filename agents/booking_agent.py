from mcp_server.core import Agent, Message
from langchain.agents import initialize_agent, AgentType
from tools.ms_booking_tool import get_booking_link
from langchain_env import llm

class BookingAgent(Agent):
    def __init__(self, runtime):
        super().__init__("booking", runtime)
        self.chain = initialize_agent([get_booking_link], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

    def receive(self, msg: Message):
        body = msg.body
        if body.get("type") == "link_request":
            key = body["topic_key"]
            reply = self.chain.run(f"return get_booking_link topic_key='{key}'")
            self.send(Message(self.name, body["user"], {"text": reply}))
