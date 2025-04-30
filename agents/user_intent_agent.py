from mcp_server.core import Agent, Message
from langchain.agents import initialize_agent, AgentType
from langchain import PromptTemplate
from langchain_env import llm

_TOPIC_KEYMAP = {
    "land use": "land_use",
    "environmental": "environmental",
    "river": "environmental",
    "greenway": "environmental",
    "zoning": "zoning_tree",
    "tree code": "zoning_tree",
    "residential building": "residential_building",
    "commercial building": "commercial_building",
    "structural": "structural_engineering",
    "site development": "site_development",
    "residential permit": "residential_permit_tech",
    "commercial permit": "commercial_permit_tech",
    "stars": "stars",
    "water services": "water_services",
    "backflow": "water_quality_backflow",
    "sewer": "sewer_stormwater",
    "stormwater": "sewer_stormwater",
    "fire": "fire_safety",
    "transportation residential": "transportation_residential",
    "transportation commercial": "transportation_commercial",
    "urban forestry": "urban_forestry",
    "mechanical": "mechanical_engineering",
    "land division": "land_division",
    "design": "design_historic",
    "historic": "design_historic"
}

class UserIntentAgent(Agent):
    def __init__(self, runtime):
        super().__init__("intent", runtime)
        self.chain = initialize_agent([], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

    def receive(self, msg: Message):
        text = msg.body.get("text", "")
        prompt = PromptTemplate.from_template(
            "Extract the topic keyword from the user message. "
            "Return JSON {{'topic':''}} where topic is one of: {topics}. "
            "User: {text}"
        ).format(topics=", ".join(_TOPIC_KEYMAP.keys()), text=text)

        resp = self.chain.run(prompt)
        try:
            topic_raw = eval(resp)["topic"].lower()
        except Exception:
            topic_raw = ""

        topic_key = _TOPIC_KEYMAP.get(topic_raw)
        if topic_key:
            self.send(Message(self.name, "booking", {"type": "link_request", "topic_key": topic_key, "user": msg.sender}))
        else:
            self.send(Message(self.name, msg.sender, {"text": "Sorry, could not match your request."}))
