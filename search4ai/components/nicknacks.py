import json
import re
def remove_forward_slashes(text):
    return text.replace('/', '')
def remove_back_slashes(text):
    return text.replace('\\', '')


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

def clean_data(data):
  text = re.sub(r"\[[0-9]*\]"," ",data)
  text = text.lower()
  text = re.sub(r'\s+'," ",text)
  text = re.sub(r","," ",text)
  return text