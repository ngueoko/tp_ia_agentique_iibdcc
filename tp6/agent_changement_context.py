from langchain_ollama import ChatOllama 
from langchain.agents import create_agent
from colorContext import ColourContext
from langchain.tools import tool, ToolRuntime

model = ChatOllama(
model="llama3.2", # ou mistral, gemma, etc.
)

@tool
def get_favourite_colour(runtime: ToolRuntime) -> str:
    """Get the favourite colour of the user"""
    return runtime.context.favourite_colour

    
@tool
def get_least_favourite_colour(runtime: ToolRuntime) -> str:
    """Get the least favourite colour of the user"""
    return runtime.context.least_favourite_colour

agent = create_agent(model=model,
                     tools=[get_favourite_colour, get_least_favourite_colour],
context_schema=ColourContext)

from langchain.messages import HumanMessage

response = agent.invoke(
{"messages": [HumanMessage(content="What is my favorite colour?")]},
context=ColourContext(favourite_colour="green")
)
print(response['messages'][-1].content)
                             