import os
import json
from datetime import datetime
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.llms import Ollama
from langchain_community.tools.tavily_search import TavilySearchResults

# Initialize the LLM and Tavily search tool
llm = Ollama(model="mistral")
tavily_tool = TavilySearchResults(
    name="web_search",
    description="Search the web for current information"
)

# Prefix to guide the agent's reasoning
prefix = """You are an AI research assistant. Use the tool `web_search` to gather live web information.

ALWAYS follow this strict format:

Thought: What are you thinking?
Action: web_search
Action Input: the exact search phrase

Then wait for the Observation before continuing.
If you know the answer already, skip the Action and just respond.

Only use tools listed. Do not invent tool names.
"""

# Initialize the agent
research_agent = initialize_agent(
    tools=[tavily_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
    agent_kwargs={"prefix": prefix}
)

# Function to save research output into a file
def save_research_output(query: str, response: str):
    os.makedirs("research_output", exist_ok=True)
    filename = f"research_output/{datetime.now().strftime('%Y%m%d_%H%M%S')}_research.json"
    with open(filename, "w") as f:
        json.dump({"query": query, "response": response}, f, indent=4)

# Function to run the research agent
def run_research_agent(query: str) -> str:
    try:
        # Run the research agent and get the response
        response = research_agent.run(query)

        # Check if the response contains the proper action format
        if 'Action' in response and 'Action Input' in response:
            action = response['Action']
            action_input = response['Action Input']
            print("Action:", action)
            print("Action Input:", action_input)
        else:
            print("Error: Missing Action or Action Input in response")

        # Save the research output to a file
        save_research_output(query, response)
        return response
    except Exception as e:
        print(f"Error in run_research_agent: {e}")
        return f"Error occurred: {e}"
