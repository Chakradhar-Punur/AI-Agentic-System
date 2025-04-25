import streamlit as st
from workflows.langgraph_workflow import graph

st.title("LangGraph Research Assistant")

query = st.text_input("Enter your research question:")

if "graph_state" not in st.session_state:
    st.session_state.graph_state = {"history": []}

if st.button('Get Answer'):
    if query:
        with st.spinner("Processing..."):
            st.session_state.graph_state["query"] = query
            result = graph.invoke(st.session_state.graph_state)
            st.session_state.graph_state.update(result)
            
            st.success("Done!")

            st.markdown("#### Final Answer")
            st.write(result["final_answer"])
            st.divider()
    else:
        st.error("Please enter a research question.")

if st.button('Reset History'):
    st.session_state.graph_state = {"history": []}
    st.success("History reset successfully.")
    st.write("You can start a new research question.")

if st.button('Show History'):
    st.subheader("Conversation History:")
    for turn in st.session_state.graph_state.get("history", []):
        if "query" in turn:
            st.markdown(f"**You:** {turn['query']}")
        if "answer" in turn:
            st.markdown(f"**Assistant:** {turn['answer']}")
