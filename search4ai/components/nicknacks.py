import json
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


print(remove_non_json_text('"I apologize for the mistake!\n\n`{ \"FUNCTION\": \"READ\", \"DATA\": \"yr.no\" }`\n\nPlease wait for the server response..."'))