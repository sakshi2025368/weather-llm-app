import os
from langchain_openai import ChatOpenAI
from backend.tools import get_weather

# Directly set your API keys
OPENROUTER_API_KEY = "sk-or-v1-660...cd30239"  # Replace with your full OpenRouter key

# Define the LLM using the key directly
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=OPENROUTER_API_KEY,
    temperature=0
)

# Function to run the agent
def run_agent(query: str) -> str:
    """
    The agent will handle user queries about weather.
    """
    # If user asks about weather, we use get_weather
    if "weather" in query.lower():
        # extract city from query (simple approach)
        words = query.split()
        city = words[-1]  # assume last word is city
        return get_weather(city)
    
    # For general queries, use the LLM directly
    return llm(query)
