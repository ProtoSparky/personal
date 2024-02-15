import requests
from ollama import Client
api_domain = "http://192.168.50.197:11434/api"

message = {'role': 'user', 'content': 'Why is the sky blue?'}
response = Client(api_domain).chat(model='llama2', messages=[message])




