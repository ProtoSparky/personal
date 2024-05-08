from ollama import Client
import json 
API_location = "http://192.168.50.220:11434/api"
model = "llama3"
memory_area = "./memory.json"
system_msg_str = """You are a helpful assistant"""
system_MSG = {"role": "system", "content": system_msg_str}
#MSG GET/WRITE
def read_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("An error occurred:", str(e))
        return None
#############################################
def write_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("An error occurred:", str(e))

def write_json_blind(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        None 

def read_json_blind(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return None
#############################################

def MSG_AI(model):
    SetupStorage()
    user_input = input(">>> Send message to AI ") 
    msg = {"role": "user", "content": user_input}
    history = read_json(memory_area)
    history.append(msg)

    response = Client(API_location).chat(model=model, messages=history)
    response_clean = response["message"]
    #save prompt
    history.append(response_clean)
    write_json(history, memory_area)
    ProcessRequest(response_clean)


def SetupStorage():
    #this function sets up the JSON file if it does not exist at the time of message send
    history = read_json_blind(memory_area)
    if(history == None):
        #create file
        print("Setting up history storage...")
        temp_storage = []
        temp_storage.append(system_MSG)
        write_json_blind(temp_storage, memory_area)
    elif(len(history) < 1):
        temp_storage = []
        temp_storage.append(system_MSG)
        write_json(temp_storage, memory_area)


def ProcessRequest(response):
    print("AI>>>" + str(response["content"]))
    MSG_AI(model)

MSG_AI(model)