import subprocess
import platform
import re

from urllib.parse import urlparse


def ping_server(host):
    """
    Pings a server and returns the ping time in milliseconds or None if the server cannot be found.
    """
    # Parse the host URL to extract the domain or IP address
    parsed_host = urlparse(host)
    # If a scheme is present, use the netloc attribute to get the hostname or IP address
    # If no scheme is present, use the host as is
    hostname = parsed_host.netloc if bool(parsed_host.scheme) else host

    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', hostname]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print("OWO" + output)
        # Extracting the time value from the output
        if 'time=' in output:
            time_index = output.find('time=') +   5
            time_value = output[time_index:].split()[0]
            print("FUCK!" + time_value)
            # Returning the time in milliseconds
            return extract_number_from_ping(time_value)
    except subprocess.CalledProcessError:
        pass  # Server not found, return None
    return None


def is_alive(host):
    # Parse the host URL to extract the domain or IP address
    parsed_host = urlparse(host)
    # If a scheme is present, use the netloc attribute to get the hostname or IP address
    # If no scheme is present, use the host as is
    hostname = parsed_host.netloc if bool(parsed_host.scheme) else host

    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', hostname]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        # Extracting the time value from the output
        if 'time=' in output:
            return True
    except subprocess.CalledProcessError:
        pass  # Server not found, return None
    return False






def extract_number_from_ping(ping_string):
    # Use regex to find all digits in the string
    numbers = re.findall(r'\d+', ping_string)
    # Since you're interested in the first number, convert it to an integer
    return int(numbers[0]) if numbers else None

print(is_alive("https://google.com"))