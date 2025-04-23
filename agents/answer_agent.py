import os
import json
from datetime import datetime
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import GPT4All
from langchain_core.runnables import RunnableSequence

llm = GPT4All(model="/Users/Chakradhar/AI_Agentic_System/models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", verbose=True)

template = """
Based on the following research context, answer the user's question clearly.

Research:
{context}

Question:
{query}

Answer (in a clear and complete paragraph):"""

prompt = PromptTemplate(input_variables=["context", "query"], template=template)

# Create the sequence of operations
answer_agent = prompt | llm

# Saving the generated answer for traceability
def save_answer_output(context: str, query: str, answer: str):
    os.makedirs("research_output", exist_ok=True)
    filename = f"research_output/{datetime.now().strftime('%Y%m%d_%H%M%S')}_answer.json"
    with open(filename, "w") as f:
        json.dump({"context": context, "query": query, "answer": answer}, f, indent=4)

# Main function to generate the answer
def generate_answer(context: str, query: str) -> str:
    response = answer_agent.invoke({"context": context, "query": query})
    
    if not response.strip().endswith('.'):
        response += " [The model response might be incomplete.]"

    save_answer_output(context, query, response)
    return response
