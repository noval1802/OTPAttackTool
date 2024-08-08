import sys
import subprocess

try:
    import requests
    import time
    import random
    import os
    import urllib3
    import json
    import bs4
    
except ImportError as e:
    print(f"error importing module:{e}")
    sys.exit(1)

finally:
    import requests
    import urllib3
    from bs4 import BeautifulSoup as bs

def banner():
    ascii_art = """ 
  ____  _________  ___  __  __           __  ______          __
 / __ \/_  __/ _ \/ _ |/ /_/ /____ _____/ /_/_  __/__  ___  / /
/ /_/ / / / / ___/ __ / __/ __/ _ `/ __/  '_// / / _ \/ _ \/ / 
\____/ /_/ /_/  /_/ |_\__/\__/\_,_/\__/_/\_\/_/  \___/\___/_/  
  
    """
    print(ascii_art)
    
from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs
from requests import post,get

green   = "\033[1;92m"
white   = "\033[1;97m"
gray    = "\033[1;90m"
yellow  = "\033[1;93m"
purple  = "\033[1;95m"
red     = "\033[1;91m"
blue    = "\033[1;96m"

def typing(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)
        
def countdown(time_sec):
        mins, secs = divmod(time_sec,60)
        timeformat = '\033[1;93m \033[1;97m] Please Wait For The Process \033[1;92 {:02d}:{:02d}]'