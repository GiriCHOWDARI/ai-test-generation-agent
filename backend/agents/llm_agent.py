import os
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

# Fallback to the model you confirmed is installed
DEFAULT_MODEL = "deepseek-coder:6.7b-instruct-q4_K_M"
model_name = os.getenv("OLLAMA_MODEL", DEFAULT_MODEL)

llm = ChatOllama(model=model_name, temperature=0)

def generate_tests(prompt: str) -> str:
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content