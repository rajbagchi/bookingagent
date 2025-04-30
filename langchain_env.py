from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory

llm = AzureChatOpenAI(
    deployment_name="gpt-4o",   # change to your deployment
    model_name="gpt-4-1106-preview",
    temperature=0.2,
)
memory = ConversationBufferMemory(return_messages=True)
