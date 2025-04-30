from mcp_server.runtime import Runtime
from mcp_server.core import Message
from agents.user_intent_agent import UserIntentAgent
from agents.booking_agent import BookingAgent

rt = Runtime()
UserIntentAgent(rt)
BookingAgent(rt)

rt.post(Message("user1", "intent", {"text": "I need a zoning appointment"}))
for _ in range(30):
    rt.step()
