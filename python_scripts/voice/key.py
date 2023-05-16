import keyboard
import time
from functionality import openapp, sing,search_for
from database import search_keys

def bind(action):
    check = 1

    if("open app" in action.lower()):
        openapp(action)
    elif("search for" in action.lower()):
        search_for(action)
    else:
        key = search_keys(action.lower())
        keyboard.press_and_release(key)
    

    if(not check):
        time.sleep(2)
