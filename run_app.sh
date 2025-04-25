#!/bin/bash

echo "🚀 Starting Ollama with Mistral model..."
ollama serve &
ollama run mistral &

# Wait for Ollama to start (usually takes a few seconds)
echo "⏳ Waiting for Ollama to initialize..."
sleep 5  # Adjust if needed

echo "💡 Starting Streamlit app..."
source venv/bin/activate
streamlit run app.py