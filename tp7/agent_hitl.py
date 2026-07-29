from langchain.agents import create_agent, AgentState
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain_ollama import  ChatOllama
from  dotenv  import load_dotenv
from tool_hitl  import read_email,send_email

load_dotenv()

class EmailState(AgentState):
    email: str


agent = create_agent(
    model="gpt-5-nano",
    tools=[read_email, send_email],
    state_schema=EmailState,
    checkpointer=InMemorySaver(),
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
            "read_email": False,
            "send_email": True,
            },
            description_prefix="Tool execution requires approval",
        ),
    ],
)