from langchain.tools import tool, ToolRuntime
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from colorContext import ColourContext
from langchain.messages import HumanMessage

@tool
def get_favourite_colour(runtime: ToolRuntime) -> str:
    """Get the favourite colour of the user"""
    return runtime.context.favourite_colour

@tool
def get_least_favourite_colour(runtime: ToolRuntime) -> str:
    """Get the least favourite colour of the user"""
    return runtime.context.least_favourite_colour

model = ChatOllama(
model="llama3.2", # ou mistral, gemma, etc.
)

agent = create_agent(
model=model,
tools=[get_favourite_colour, get_least_favourite_colour],
context_schema=ColourContext
)
response = agent.invoke(
{"messages": [HumanMessage(content="What is my favourite colour?")]},
context=ColourContext()
)
print(response['messages'][-1].content)