from ollama import Client
import json 
import components.read_website as readwsite
import components.nicknacks as nick
import components.search as search
import components.summarize as summ
import components.calc as calc
import traceback
import datetime
import os
current_datetime = datetime.datetime.now()
model = "llama3"
API_location = "http://localhost:11434/api"
memory_area = "./memory.json"
system_MSG_str = """
From now on, all communication will be in JSON format.
Your primary key is FUNCTION. Available states include:
  REPLY: respond to user's question.
  SEARCH: search google for links on a given query. This can be combined with READ to read ONE link at a time. Said link has to be a plain string
  READ: retrieve all readable text from a domain (no search engines allowed!)
  CALC: perform basic arithmetic operations (+, -, /, *). When using CALC, the DATA key cannot contain anything else other than your numbers and your arithmetic operation. "2 times 2" = wrong. "2*2" = correct
You WILL use SEARCH and or READ to get up to date information from the internet if the user's query requires that. 
When executing the *ANY* function, please respond with a JSON object that contains only one key-value pair: `FUNCTION` and `DATA`. The string in DATA should be provided as a plain string value directly in the DATA key *without* any additional nesting or comments with forward slashes. Your output CANNOT break JSON compliancy by adding ivalid characters or text before and or after the JSON string. Your text reply MIST be within DATA!
If FUNCTION contains "USER REPLY", then a user has replied. Otherwise assume that what replied to you was the server backend and not a user
Rules:
* Use only one function at a time.
* After executing, wait for server response before returning data.
* Do not execute READ or SEARCH functions with Google or other search engine domains.
* If the system returns an error, STOP, REPLY to user and ASK for guidance
Your goal is to be an educational and smart assistant. Use SEARCH and READ commands to gather up-to-date information on current matters.""" + " The current date and time is :" + current_datetime.strftime("%Y-%m-%d %H:%M:%S") + " as YYYY-MM-DD HH:MM:SS."



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
    formatting = {
        "FUNCTION":"USER REPLY",
        "SRV_RETURN":user_input
    }
    msg = {"role": "user", "content": json.dumps(formatting)}
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
    #this processes the requests 
    response_str = nick.remove_non_json_text(response["content"])
    try: 
        response_obj = CleanInput(response_str)
        if("FUNCTION" in response_obj):
            #continue execution
            data = response_obj["DATA"]
            #define functions
            if(response_obj["FUNCTION"] == "REPLY"):
                print("---" + response_obj["DATA"])
                MSG_AI(model)
            elif(response_obj["FUNCTION"] == "SEARCH"):
                #run for search
                print("Searching for... " + data)  
                queries = search.g_search(data)
                print("Found links " + str(queries))
                return2AI(queries, "SEARCH")
            elif(response_obj["FUNCTION"] == "READ"):
                #run for read
                print("Reading page... " + data)  
                web_text = summ.summarize(nick.remove_forward_slashes(readwsite.read_website(data)), sentences_count = 50)
                return2AI(web_text,"READ")
            elif(response_obj["FUNCTION"] == "CALC"):
                #run for calc
                print("using calculator for " + data)
                return2AI(calc.calculate(data), "CALC")
        else:
            print("Backend command not recognized!")
            print("----------------------------------")
            print(str(response["content"]))
            return2AI("Failed processing request. Are you sure you are proper rules for formatting the JSON command?", "ERROR")
    except Exception as e:
        print("-------------------------------ERROR-------------------------------")
        error_message = f"Error: {e}"
        print(error_message)
        tb = traceback.format_exc()
        print(tb)
        print("Failed Processing JSON")
        print("RETURN DATA")
        print(response)
        print("-------------------------------ERROR-------------------------------")
        return2AI("Failed processing request. STOP, run FUNCTION REPLY and ask user for guidance! Remember the system rules!", "ERROR")
    
def CleanInput(str):
    try:
        response_obj = json.loads(str)
        return response_obj
    except:
        #try more harsh filtering
        str.replace('“', '"')
        str.replace('”','"')
        try:
            response_obj = json.loads(str)
            return response_obj
        except:
            print("CLEAN INPUT GIVING UP")
            print(str)
            return {}


def return2AI(text, function_name):
    formatting = {
        "FUNCTION":function_name,
        "SRV_RETURN":text
    }
    msg = {"role": "user", "content": json.dumps(formatting)}
    history = read_json(memory_area)
    history.append(msg)

    response = Client(API_location).chat(model=model, messages=history)
    response_clean = response["message"]
    #save prompt
    history.append(response_clean)
    write_json(history, memory_area)
    ProcessRequest(response_clean)



#clear terminal
nick.ReadyScreen()
MSG_AI(model)
