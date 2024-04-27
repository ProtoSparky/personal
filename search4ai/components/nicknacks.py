import json
import re
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

'''
def remove_non_json_text(input_string):
    # Remove all newline characters
    input_string = input_string.replace('\n', '')

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
def remove_non_json_text(input_string):
    # Remove all newline characters
    input_string = input_string.replace('\n', '')

    # Remove comments at the start of the string
    input_string = re.sub(r'^\s*\/\/.*?(?=\{)', '', input_string)

    # Check if the string starts with '{'
    while not input_string.startswith('{') and len(input_string) > 0:
        input_string = input_string[1:]

    # Check if the string ends with '}'
    while not input_string.endswith('}') and len(input_string) > 0:
        input_string = input_string[:-1]

    # Remove comments within the JSON string
    input_string = re.sub(r'\/\/(?!.*")\s*.*?(?=\n|\Z)', '', input_string)

    print(input_string)
    # Ensure the last character is '}'
    if not input_string.endswith('}'):
        input_string += '}'

    # Try to parse the JSON
    try:
        json.loads(input_string)
    except ValueError:
        return ''

    return input_string


import re

def remove_comments_from_json_string(json_string):
    # Define a regex pattern to match text that does not fit the JSON key-value pair format
    # This pattern looks for text that does not contain a colon followed by a value
    # It also looks for text that does not contain a comma followed by a key
    pattern = r'(?<!:)\s*[^:,]*\s*(?!:)|(?<!,)\s*[^:,]*\s*(?=,)'
    
    # Use a loop to remove non-conforming text until no more matches are found
    while True:
        match = re.search(pattern, json_string)
        if match:
            # If non-conforming text is found, remove it
            json_string = json_string[:match.start()] + json_string[match.end():]
        else:
            # If no more non-conforming text is found, break the loop
            break
    
    return json_string

# Example usage
json_string = '{ //comment "FUNCTION": "READ", "DATA": "https://www.accuweather.com/en/no/oslo/254946/current-weather/254946"}'
clean_json_string = remove_comments_from_json_string(json_string)
print(clean_json_string)
