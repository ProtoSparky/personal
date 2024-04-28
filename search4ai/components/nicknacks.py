import json
import re
import os
def remove_forward_slashes(text):
    return text.replace('/', '')
def remove_back_slashes(text):
    return text.replace('\\', '')

'''
def remove_non_json_text(input_string):
    # Check if the string starts with '{'
    while not input_string.startswith('{') and len(input_string) > 0:
        input_string = input_string[1:]

    # Check if the string ends with '}'
    while not input_string.endswith('}') and len(input_string) > 0:
        input_string = input_string[:-1]

    # Try to parse the JSON
    try:
        json.loads(input_string)
    except ValueError:
        return ''

    return input_string
'''
def clean_data(data):
  text = re.sub(r"\[[0-9]*\]"," ",data)
  text = text.lower()
  text = re.sub(r'\s+'," ",text)
  text = re.sub(r","," ",text)
  return text


def remove_non_json_text(json_string):
    # Regular expression to match the JSON key-value pairs
    pattern = r'"([^"]+)":\s*("[^"]+"|true|false|null|\d+\.?\d*)'
    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, json_string)
    # Construct a new JSON string from the matches
    cleaned_json_string = "{" + ",".join(['"%s":%s' % (key, value) for key, value in matches]) + "}"
    # Try to parse the JSON
    try:
        json.loads(cleaned_json_string)
    except ValueError:
        return ''

    return cleaned_json_string 

def remove_non_json_text_arr(json_string):
    # Updated regular expression to match JSON key-value pairs and arrays
    pattern = r'"([^"]+)":\s*("[^"]+"|true|false|null|\d+\.?\d*|\[[^\]]*\])'
    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, json_string)
    # Construct a new JSON string from the matches
    cleaned_json_string = "{" + ",".join(['"%s":%s' % (key, value) for key, value in matches]) + "}"
    # Try to parse the JSON
    try:
        json.loads(cleaned_json_string)
    except ValueError:
        return ''

    return cleaned_json_string

def ReadyScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("|------------------------------------------------------------------------------------------------------------------------------------------|")
    print("|-------------------------------------------------------------------NEW CHAT---------------------------------------------------------------|")
    print("|------------------------------------------------------------------------------------------------------------------------------------------|")

def context_trimmer(memory_area): 
    def write_json(data, filename):
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print("An error occurred:", str(e))
    ############################################
    def read_json(filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print("An error occurred:", str(e))
            return []
    ############################################
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
                return {}
    ############################################

    #this function decides what needs to be trimmed from the memory storage
   
    all_context = read_json(memory_area)
    context_length = len(all_context) - 1 #without last message
    context_pointer = 1 #skip system message
    new_context = []
    new_context.append(all_context[0])
    while context_pointer < context_length:
        current_context = all_context[context_pointer]
        selected_message = current_context["content"]
        #check that current context is not the last context in the message
        if(context_pointer < context_length):
            #messages here do not include system prompt or the last message written
            message_object = CleanInput(remove_non_json_text_arr(selected_message))
            
            if(len(message_object) != 0):
                #locate all srv return objects
                if("SRV_RETURN" in message_object):
                    #object was a SRV return
                    #locate READ and SEARCH
                    '''
                    if(message_object["FUNCTION"] != "READ" or message_object["FUNCTION"] != "SEARCH"):
                        #Found SRV SEARCH and READ pages
                        new_context.append(all_context[context_pointer])                '''    
                else:
                    new_context.append(all_context[context_pointer])
        context_pointer +=1
    new_context.append(all_context[len(all_context) - 1])

    for cpointer in new_context:
        print("----\n")
        print(cpointer)
