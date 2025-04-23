import os
import json
from datetime import datetime
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.llms import GPT4All
from langchain_community.tools.tavily_search import TavilySearchResults

llm = GPT4All(model="/Users/Chakradhar/AI_Agentic_System/models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", verbose=True)
tavily_tool = TavilySearchResults(
    name="web_search",
    description="Search the web for current information"
)

research_agent = initialize_agent(
    tools=[tavily_tool],
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

def save_research_output(query: str, response: str):
    os.makedirs("research_output", exist_ok=True)
    filename = f"research_output/{datetime.now().strftime('%Y%m%d_%H%M%S')}_research.json"
    with open(filename, "w") as f:
        json.dump({"query": query, "response": response}, f, indent=4)

def run_research_agent(query: str) -> str:
    response = research_agent.run(query)
    save_research_output(query, response)
    return response
