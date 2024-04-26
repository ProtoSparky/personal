import asyncio
from ollama import AsyncClient
#api_domain = "http://192.168.50.197:11434/api"
api_domain = "http://localhost:11434/api"
#ai_model = "llama2"
ai_model = "codellama"
prompt = 'SERVER : You have been given the ability to search the web. From now on, youll be communicating using json. When a user asks a question the action key will be "question", and the question will be in "data". You can return specific actions to search the web, like "search" which allows you to send a search query to google in data, and then get a return of links related to the answer of your question.You can then ick some links from the returned list, and send them in data with the query "read". This will run curl and return you information that might help you answer the users question.Once you think you know the answer to the users quesiton, you can return "answer" in the action key, and in data return your full answer to the users question. If youve used the web, you must return the sources you used to answer the question. This can be done by adding the number of a source as a hyperlink in markdown to the end of your sentence.This is how the json format has to look:{"action":"search","data":["your search query"]}.Your valid commands are "search", "read", "answer". The server will always return the data with the action key "return", and when a user asks a question, the action will be "question". The data key is used for all information like your search queries, html data from websites, and your answers. You may now answer the users question as concisely as possible. USER: {"action":"question","data":["What is currently happening in norway?"]}'

async def chat():
  message = {'role': 'user', 'content': prompt}
  async for part in await AsyncClient(api_domain).chat(model=ai_model, messages=[message], stream=True):
    print(part['message']['content'], end='', flush=True)

asyncio.run(chat())