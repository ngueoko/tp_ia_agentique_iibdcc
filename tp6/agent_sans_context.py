from colorContext  import ColourContext
from langchain_ollama import ChatOllama 
from langchain.agents import create_agent

model = ChatOllama(
model="llama3.2", # ou mistral, gemma, etc.
)

agent = create_agent(model=model,
context_schema=ColourContext)

from langchain.messages import HumanMessage

response = agent.invoke(
{"messages": [HumanMessage(content="What is my favourite colour?")]},
context=ColourContext()
)

print(response['messages'][-1].content)
                             