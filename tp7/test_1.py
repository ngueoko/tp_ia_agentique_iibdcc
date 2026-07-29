from agent_hitl  import agent


from langchain.messages import HumanMessage
config = {"configurable": {"thread_id": "1"}}
response = agent.invoke(
{
"messages": [HumanMessage(content="Veuillez lire mon e-mail et envoyer " \
"une réponse immédiatement. Envoyez la réponse maintenant dans le même fil de " \
"discussion.")], 
"email": "Bonjour Sara, je vais être en retard pour notre réunion de demain. Pouvons-nous la reprogrammer ? Cordialement, Sofia"
},
config=config
)
print(f"Response : ",response)
print("_________________________________________________________________________________________________________________________________________________")
#Afficher le message interrompu avec metadata
print(" Interupt : ",response['__interrupt__'])
print("_________________________________________________________________________________________________________________________________________________")
print(response['__interrupt__'][0].value['action_requests'][0]['args']['body'])