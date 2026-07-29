import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from sous_agent_calcul import subagent_1,subagent_2
from langchain.messages import HumanMessage
from langchain.agents import create_agent
from langchain.tools import tool


# Charger les variables d'environnement (.env)

@tool
def call_subagent_1(x: float) -> float:
    """Call subagent 1 in order to calculate the square root of a number"""
    response = subagent_1.invoke({"messages": [HumanMessage(content=f"Calculate the square root of {x}")]})
    return response["messages"][-1].content

@tool
def call_subagent_2(x: float) -> float:
    """Call subagent 2 in order to calculate the square of a number"""
    response = subagent_2.invoke({"messages": [HumanMessage(content=f"Calculate the square of {x}")]})
    return response["messages"][-1].content

main_agent = create_agent(
    model='gpt-5-nano',
    tools=[call_subagent_1, call_subagent_2],
    system_prompt="You are a helpful assistant who can call subagents to calculate the square root or square of a number."
    )