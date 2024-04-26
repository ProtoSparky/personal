
from ollama import Client
api_domain = "http://localhost:11434/api"

message2 = {'role': 'user', 'content': 'Why is the sky blue'}
message1 = {'role': 'assistant', 'content': 'The sky appears blue because of a phenomenon called Rayleigh scattering, which occurs when sunlight travels through the Earths atmosphere.'}
message = {'role': 'system', 'content': 'What was the last thing you told the user?'}
response = Client(api_domain).chat(model='llama3', messages=[message2, message1,message])
print(response)




