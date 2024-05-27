from ollama import Client
import tools as tk
import getpass
import json
username = getpass.getuser()
llamaAPI = "192.168.50.220:11434/api"
llama_model = "llama3"
file_path = f"C:\\Users\\{username}\\Downloads\\ssid2.csv"


def rater(ssid):
    ## Ask AI to rate ssid
    stock_ssid = ["AirTies%&", "Air%&", "TP-Link%&", "Telia%&", "Telenor%&", 
                  "GNX%&", "Getbox%&", "NextGenTel%&", "DIRECT%&","Home_Net%&","Zyxel%&", "NETGEAR%&"]
    system_msg = """Your job is to rate the wifi SSID the user sends from 0 to 10 by creativity. 
    If the SSID is a default one, rate it negative 1. 
    You myst ONLY reply with the intiger, and nothing more.
    """
    system_msg_obj = {"role":"system", "content":system_msg}
    user_msg_obj = {"role":"user", "content":ssid}
    total_msg = []
    total_msg.append(system_msg_obj)
    total_msg.append(user_msg_obj)
    response = Client(llamaAPI).chat(model=llama_model, messages=total_msg)
    return response["message"]["content"]
    


def filter():
    for current_line in tk.read_file_by_lines(file_path):
        if(current_line != ""):
            print(current_line)

filter()