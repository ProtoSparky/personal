from ollama import Client
import tools as tk
import getpass
import json
username = getpass.getuser()
llamaAPI = "192.168.50.220:11434/api"
llama_model = "llama3"
file_path = f"C:\\Users\\{username}\\Downloads\\ssid2.csv"
stock_ssid = ["AirTies", "Air", "TP-Link", "Telia", "Telenor", 
"GNX", "Getbox", "NextGenTel", "DIRECT","Home_Net","Zyxel", "NETGEAR", "Altibox", 
"ASUS", "dlink", "TP-LINK", "Osloskolen", "GET", "Get", "linksys", "REMOTE", "HP-", "Omni", "ok-"]


def rater(ssid):
    ## Ask AI to rate ssid
    system_msg = """Your job is to rate the wifi SSID the user sends from 0 to 10 by creativity. 
    If the SSID is a default one, rate it -1. When it comes to creativity, it's ok if the name contains 'wifi' or the frequency. What matters is if it's fun, quirky, hilarios, and so on. Rate it by the content of the name
    You myst ONLY reply with the intiger, and nothing more.
    """
    system_msg_obj = {"role":"system", "content":system_msg}
    user_msg_obj = {"role":"user", "content":ssid}
    total_msg = []
    total_msg.append(system_msg_obj)
    total_msg.append(user_msg_obj)
    response = Client(llamaAPI).chat(model=llama_model, messages=total_msg)
    try: 
        return response["message"]["content"]
    except:
        print(response)
    
def matcher(input_str, arr2match):
    for element in arr2match:
        if element in input_str:
            return True
    return False

def filter():
    new_arr = []
    for current_line in tk.read_file_by_lines(file_path):
        if(current_line != ""):
            if(matcher(current_line, stock_ssid)):
                pass
            else:
                new_arr.append(current_line)

    return new_arr




tmp_array = []
counter = 0
filtered = filter()
for current_network in filtered:
    rated = rater(current_network)
    network = {current_network : rated}
    print(str(network) + str(counter) + "/" + str(len(filtered)))
    tmp_array.append(network)
    counter += 1
print(tmp_array)
    