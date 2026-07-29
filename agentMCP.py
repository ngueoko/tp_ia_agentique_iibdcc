import asyncio

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():

    # Configuration du serveur MCP
    client = MultiServerMCPClient(
        {
            "local_server": {
                "transport": "stdio",
                "command": "python",
                "args": ["resources/mcp_local_server.py"],
            }
        }
    )

    # Récupération des outils du serveur MCP
    tools = await client.get_tools()

    # Récupération des ressources (optionnel)
    resources = await client.get_resources("local_server")
    print(resources)

    # Récupération du prompt système
    prompt = await client.get_prompt(
        "local_server",
        "prompt"
    )

    system_prompt = prompt[0].content

    # Initialisation du modèle Ollama
    model = ChatOllama(
        model="llama3.2",
        temperature=0,
    )

    # Création de l'agent
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
    )

    config = {
        "configurable": {
            "thread_id": "1"
        }
    }

    # Exécution de l'agent
    response = await agent.ainvoke(
        {
            "messages": [
                HumanMessage(
                    content="Tell me about the langchain-mcp-adapters library"
                )
            ]
        },
        config=config,
    )

    print(response["messages"][-1].content)



asyncio.run(main())