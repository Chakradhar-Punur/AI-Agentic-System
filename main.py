from workflows.langgraph_workflow import graph
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

# Getting the user’s query from input
query = input("Enter your research question: ")

# Running the LangGraph workflow
result = graph.invoke({"query": query})

# Displaying the final answer
print("\nFinal Answer:\n", result["final_answer"])
