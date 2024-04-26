from ollama import Client
import json 
import components.read_website as readwsite
import components.nicknacks as nick

model = "llama3"
API_location = "http://localhost:11434/api"
memory_area = "./memory.json"

system_MSG_str = """
From now on, all communication will be in JSON format.

Your primary key is FUNCTION. This key can have multiple states, including:


    REPLY: replies to the user's question and stores the response in the DATA key.

    SEARCH: returns links from any search query performed within the DATA key.

    READ: takes a domain as input and returns the website's content as readable text stored in the DATA key.

    CALC: performs basic arithmetic operations (+, -, /, *) on mathematical equations and returns the result.


Important:


    The AI will only use one function at a time.

    After executing a function, the server will reply with data.

    The AI is then allowed to return data to the user.

    Only one function can be executed at a time. If you need to perform another action, please execute the new function and wait for the response from the server.

    When executing the *ANY* function, please respond with a JSON object that contains only one key-value pair: `FUNCTION` and `DATA`. The string in DATA should be provided as a plain string value directly in the DATA key *without* any additional nesting.


Your goal is to be an educational and smart assistant. You will use the internet with the SEARCH and READ commands to gather up-to-date information on current matters."""


system_MSG = {"role": "system", "content": system_MSG_str}




####
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
#############################################




def MSG_AI(model):
    SetupStorage()
    user_input = input("Send message to AI ") 
    msg = {"role": "user", "content": ""}
    msg["content"] = user_input
    history = read_json(memory_area)
    history.append(msg)
    response = Client(API_location).chat(model=model, messages=history)
    response_clean = response["message"]
    #save prompt
    history.append(response_clean)
    write_json(history, memory_area)

    ProcessRequest(response_clean)
    #print(response_clean)

def SetupStorage():
    #this function sets up the JSON file if it does not exist at the time of message send
    history = read_json(memory_area)
    if(history == None):
        #create file
        print("Setting up history storage...")
        temp_storage = []
        temp_storage.append(system_MSG)
        write_json(temp_storage, memory_area)
    elif(len(history) < 1):
        temp_storage = []
        temp_storage.append(system_MSG)
        write_json(temp_storage, memory_area)

def ProcessRequest(response):
    #this processes the requests 
    response_str = response["content"]
    response_obj = json.loads(response_str)
    if("FUNCTION" in response_obj):
        #continue execution
        data = response_obj["DATA"]

        #define functions
        if(response_obj["FUNCTION"] == "REPLY"):
            print(response_obj["DATA"])
        elif(response_obj["FUNCTION"] == "SEARCH"):
            #run for search
            print("want2 searcch")
        elif(response_obj["FUNCTION"] == "READ"):
            #run for read
            web_text = nick.remove_forward_slashes(readwsite.read_website(data))
            return2AI("READ",web_text)

        elif(response_obj["FUNCTION"] == "CALC"):
            #run for calc
            print("want2caslc")
    else:
        print("Shits fucked. " + response_obj)
    

def return2AI(text, function_name):
    formatting = {
        "FUNCTION":function_name,
        "SRV_RETURN":text
    }
    msg = {"role": "system", "content":formatting }
    history = read_json(memory_area)
    history.append(msg)
    print(json.dumps(msg, indent=4))
    response = Client(API_location).chat(model=model, messages=history)
    response_clean = response["message"]
    #save prompt
    history.append(response_clean)
    write_json(history, memory_area)


MSG_AI(model)


