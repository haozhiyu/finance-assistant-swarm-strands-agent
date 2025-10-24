#!/usr/bin/env python3
"""
Finance Assistant Swarm Agent

A collaborative swarm of specialized agents for comprehensive stock analysis.
"""
# Standard library imports
import logging
import time
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters
from strands.models import BedrockModel
import os



# Bedrock
bedrock_model = BedrockModel(
  model_id="arn:aws:bedrock:us-west-2:032304891690:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0",
  temperature=0.1,
  streaming=True, # Enable/disable streaming
  region_name='us-west-2'
)

# Set AWS region for MCP client
os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'

# MCP client with uvx
aws_eks_mcp_client_uv = MCPClient(
    lambda: stdio_client(StdioServerParameters(
        command="uvx", 
        args=["awslabs.eks-mcp-server@latest"]
        )
    )
)


app = BedrockAgentCoreApp()


@app.entrypoint
def agent_invocation(payload):
    """Handler for agent invocation"""
    try:
        user_message = payload.get(
            "prompt", "No prompt found in input, please guide customer to create a json payload with prompt key"
        )
        
        with aws_eks_mcp_client_docker:
            tools = aws_eks_mcp_client_docker.list_tools_sync()
            agent = Agent(model=bedrock_model, tools=tools)
            response = agent(user_message)
            return {"response": str(response)}
        
        # test with no mcp client
        # agent = Agent(model=bedrock_model)
        # response = agent(user_message)
        # return {"response": str(response)}

    except Exception as e:
        return {"error": f"Agent invocation failed: {str(e)}"}




if __name__ == "__main__":
    app.run()