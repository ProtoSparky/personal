import httpx
from pydantic import BaseModel
from httpx import ReadTimeout
import time 

# Define the base URL for your custom Ollama API
api_domain = "http://192.168.50.197:11434"

MAX_RETRIES =  100
RETRY_DELAY =  50  # Delay in seconds between retries

def custom_ollama_chat(model: str, messages: list) -> dict:
    request_url = f"{api_domain}/api/chat"
    request_data = {"model": model, "messages": messages}
    
    for _ in range(MAX_RETRIES):
        try:
            response = httpx.post(request_url, json=request_data, timeout=10.0)
            response.raise_for_status()  # Raise an exception if the request was unsuccessful
            return response.json()
        except ReadTimeout:
            # Log the timeout and wait before retrying
            print(f"Request timed out. Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
        except Exception as e:
            # Handle other exceptions
            print(f"An error occurred: {e}")
            break

    print("All attempts failed.")
    return {}

# Usage
response = custom_ollama_chat('llama2', [{'role': 'user', 'content': 'Why is the sky blue?'}])
if response:
    print(response['message']['content'])
else:
    print("Failed to get a response.")