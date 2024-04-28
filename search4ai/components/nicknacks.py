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

def ReadyScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("|------------------------------------------------------------------------------------------------------------------------------------------|")
    print("|-------------------------------------------------------------------NEW CHAT---------------------------------------------------------------|")
    print("|------------------------------------------------------------------------------------------------------------------------------------------|")

input = '{     "FUNCTION": "READ", "DATA": "The weather forecast for Narvik shows a mix of sunshine and cloudy skies. Temperatures range from 9 to 12 degrees Celsius with moderate winds." }'
print(remove_non_json_text(input))