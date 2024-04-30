#This is a general playground for testing if functions work the way i want them to
from ollama import Client
import requests
from bs4 import BeautifulSoup
import html2text

from llama_index.llms import Ollama
from llama_index.agent import ReActAgent
from llama_index.tools import FunctionTool
from datetime import date

def add_numbers(a : int, b: int) -> int:
    """Adds two numbers and returns the result"""
    return a+b

def get_current_date() -> date:
    """returns the current date"""
    return date.today()

tools = [
    FunctionTool.from_defaults(fn=add_numbers),
    FunctionTool.from_defaults(fn=get_current_date)
]

llm = Ollama(model="mistral")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)
response = agent.chat("what is today's date?")