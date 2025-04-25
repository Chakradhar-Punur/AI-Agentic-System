# AI-Agentic-System

## AI Agentic System with LangGraph, GPT4All & Streamlit

This project is a dual-agent research assistant powered by LangChain, LangGraph, and a local LLM (TinyLlama via GPT4All). It uses web search tools to gather information and a prompt-based answer engine to provide complete, contextual responses — all wrapped in a Streamlit front-end.

## Features

- **Research Agent** — Uses Tavily API to search the web for current and reliable information.
- **Answer Agent** — Uses GPT4All (TinyLlama model) to generate responses based on research context.
- **LangGraph Workflow** — Connects agents into a sequential graph with persistent memory.
- **State Persistence** — Maintains conversation history and allows follow-up queries.
- **Streamlit UI** — Provides a clean, user-friendly interface for interactive exploration.

## Tech Stack

- **LangChain** & **LangGraph** — Agent framework + state orchestration
- **GPT4All / TinyLlama** — Local LLM for response generation
- **Tavily API** — Real-time web search tool
- **Streamlit** — Front-end for interactive usage
- Python 3.9+

## Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/Chakradhar-Punur/AI-Agentic-System.git
cd AI-Agentic-System
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Pull the Mistral model using Ollama

Make sure you have [Ollama](https://ollama.com/) installed, then run:

```
ollama pull mistral
```

> This ensures the required model is available locally via Ollama.

### 5. Start the full system (Ollama + Streamlit) using:

```
./run_app.sh
```

> This script automatically starts the Ollama server with the Mistral model and launches the Streamlit app.


## Usage

1. Ask a question like:

“How is AI used in cancer detection?”

2. Ask a follow-up:

“How accurate is it?”

3. Click Show History to view the conversation
4. Click Reset History to start fresh


## Credits

Developed by Chakradhar as part of an internship assignment, showcasing AI-driven autonomous agents using LangGraph and local inference.
