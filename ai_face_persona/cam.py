from dotenv import load_dotenv
import os
# from web_sac_prat import flash
import requests
load_dotenv()

# class flash:
#     def on(self):
#         r = requests.get(f"{os.getenv("ip")}/enabletorch")
#     def off(self):
#         r = requests.get(f"{os.getenv("ip")}/disabletorch")

def ip():
    return os.getenv("ip_video") 

