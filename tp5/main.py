
from agent_principal import main_agent
from langchain.messages import HumanMessage

question = "What is the square root of 456?"
response = main_agent.invoke({"messages": [HumanMessage(content=question)]})
print(response['messages'][-1].content)