from tool_calcul import square_root, square
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from pathlib import Path

# Charger les variables d'environnement (.env)
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

model = ChatOllama(
model="llama3.2",
)

subagent_1 = create_agent(
model='gpt-5-nano',
tools=[square_root]
)
subagent_2 = create_agent(
model='gpt-5-nano',
tools=[square]
)