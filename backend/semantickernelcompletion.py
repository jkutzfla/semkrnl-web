import sys
import asyncio
from azure.identity.aio import DefaultAzureCredential
from semantic_kernel.agents.azure_ai import AzureAIAgent

AGENT1_ID = "asst_5Af1f1SqPcbXKLGlQG3bSOyR" #a test agent that will say PASSTO_AGENTNAME
AGENT1_ID = "asst_nn5W2GMJBtFZdKbjJ45c177Z" #ChemNovus HR Q&A Main Agent, in the ChemNovus project
AGENT1_ID = "asst_MiosvJFjX8XjDwTKzCHj3NSc" #Contoso_Sales_Agent

AGENT1_ID = "asst_WLdYwKlxTsYKDeyNrvlJj4OY" #Agent376_With_knowledge
SUBAGENT_WORD = "PASSTO_"
subagents = {
    'ONBOARDING': "asst_aFZH4PK0pfzYIuANZT46gJVP",
    'PERFREVIEW': "asst_rV1bE7sXFqoVtFZqbKuO0Qqn",
}

async def completion(question: str) -> str:
    # Use asynchronous context managers to authenticate and create the client.
    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(credential=creds) as client,
    ):
        # 1. Retrieve the agent definition based on the assistant ID.
        #    Replace "asst_MwpyijFo7T4MEzwvS8Pb5F98" with your actual assistant ID.
        agent_definition = await client.agents.get_agent(AGENT1_ID)
        # 2. Create a Semantic Kernel agent using the retrieved definition.
        agent = AzureAIAgent(client=client, definition=agent_definition)
        # 3. Create a new conversation thread.
        thread = await client.agents.create_thread()

        try:
            await agent.add_chat_message(thread_id=thread.id, message=question)

            # 5. Retrieve and print the agent's response.
            response = await agent.get_response(thread_id=thread.id)
            print(f"#Response Object: {response}")
            
            # now need a way to call sub-agents.
            if (SUBAGENT_WORD in response.__str__()):
                print(f"Detected a PASSTO_ in the response.")

                if ("PASSTO_ONBOARDING" in response.__str__()):
                    subagent_id = subagents["ONBOARDING"]
                elif ("PASSTO_PERFREVIEW" in response.__str__()):
                    subagent_id = subagents["PERFREVIEW"]
                else:
                    subagent_id = AGENT1_ID
                agent2_definition = await client.agents.get_agent(subagent_id)
                agent2 = AzureAIAgent(client=client, definition=agent2_definition)
                
                await agent2.add_chat_message(thread_id=thread.id, message=question)
                response = await agent2.get_response(thread_id=thread.id)

            return response.__str__()
        finally:
            # 6. Cleanup: Delete the conversation thread.
            await client.agents.delete_thread(thread.id)
            # Note: The agent is not deleted so it can be reused later.

if __name__ == "__main__":
    question = "Gimme a random number?"
    if len(sys.argv) > 1:
        question = sys.argv[1]

    response = asyncio.run(completion(question=question))
    print(f"#Agent: {response}")