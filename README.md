# Azure AI Agent Service Demo

Experiment with calling multiple Azure AI Service Agents

Big Picture:

* Create agents in the Agent Playground
* Get their ID
* Create basic orchestration flow in Semantic Kernel, using semantic_kernel.agents.azure_ai.AzureAIAgent (Python)
* embed AgentID into Semantic Kernel code
* Deploy as Flask backend and bare-bonus frontend
* Create Entra service principal and grant "Azure AI Developer" RBAC to the RG scope of the Foundry project and hub.
* Deploy as Container App
