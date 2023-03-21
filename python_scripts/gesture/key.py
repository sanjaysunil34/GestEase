import keyboard
from time import sleep
from database import search_keys
import os
from win10toast import ToastNotifier

def notify(action):
    dirname = os.path.dirname(__file__)
    new=dirname+'/assets/logo.ico'

    toaster = ToastNotifier()
    toaster.show_toast(msg=action.lower(),
                    title="Gesture detected",
                    icon_path=new,
                    duration=5,
                    threaded=True)
    # Wait for threaded notification to finish
    while toaster.notification_active(): sleep(0.1)

def bind(action):
    # print(action)
    notify(action)
    key=search_keys(action.lower())
    keyboard.press_and_release(key)
    sleep(2)