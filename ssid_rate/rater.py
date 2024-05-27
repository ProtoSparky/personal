from ollama import Client
llamaAPI = "./192.168.50.220:11434/api"

def rater(ssid):
    ## Ask AI to rate ssid
    system_msg = """test"""
    system_msg_obj = {"role":"system", "content":system_msg}
    user_msg_obj = {"role":"user", "content":ssid}
    total_msg = {}
    total_msg.append(system_msg_obj)
    total_msg.append(user_msg_obj)
    
