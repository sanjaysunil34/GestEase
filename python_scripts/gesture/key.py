import keyboard
from time import sleep
from database import search_keys
import os
from win10toast import ToastNotifier
import sys

def notify(action):
    dirname = os.path.dirname(__file__)
    new=dirname+'/assets/logo.ico'

    toaster = ToastNotifier()
    toaster.show_toast(msg=action.lower(),
                    title="Gesture detected",
                    icon_path=new,
                    duration=0,
                    threaded=True)  
    # Wait for threaded notification to finish
    while toaster.notification_active(): sleep(2)

def bind(action):
    # print(action)
    
    # print("action : " + action.lower())
    # sys.stdout.flush()
    key = search_keys(action.lower())
    notify(action)
    # print(key)
    # sys.stdout.flush()
    keyboard.press_and_release(key)
    #sleep(2)