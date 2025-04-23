from typing import TypedDict
from langgraph.graph import StateGraph
from agents.research_agent import run_research_agent
from agents.answer_agent import generate_answer

# Define the state schema
class ResearchState(TypedDict):
    query: str
    context: str
    final_answer: str
    history: list[dict]

# Initialize the StateGraph with the state schema
workflow = StateGraph(ResearchState)

def research_node(state):
    query = state["query"]
    context = run_research_agent(query)
    history = state.get("history", [])
    history.append({"role": "user", "query": query, "context": context})
    return {"query": query, "context": context, "history": history}

def answer_node(state):
    answer = generate_answer(state["context"], state["query"])
    history = state.get("history", [])
    history.append({"role": "assistant", "answer": answer})
    return {"final_answer": answer, "history": history}

workflow.add_node("research", research_node)
workflow.add_node("answer", answer_node)
workflow.set_entry_point("research")
workflow.add_edge("research", "answer")
workflow.set_finish_point("answer")

graph = workflow.compile()
