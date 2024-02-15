import asyncio
from ollama import AsyncClient
api_domain = "http://192.168.50.197:11434/api"
async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  async for part in await AsyncClient(api_domain).chat(model='llama2', messages=[message], stream=True):
    print(part['message']['content'], end='', flush=True)

asyncio.run(chat())