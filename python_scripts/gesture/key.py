import keyboard
from time import sleep
from database import search_keys
import os
from win10toast import ToastNotifier
import pyttsx3

def notify(action):
    dirname = os.path.dirname(__file__)
    new=dirname+'/assets/logo.ico'

    toaster = ToastNotifier()
    toaster.show_toast(msg=action.lower(),
                    title="Gesture detected",
                    icon_path=new,
                    duration=0.1,
                    threaded=True)  
    # Wait for threaded notification to finish
    while toaster.notification_active(): sleep(2)

def sound_notification(action):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    rate = engine.getProperty('rate') 
    print (rate) 
    engine.setProperty('rate', 150) 
    engine.setProperty('voice', voices[1].id) 
    engine.say("Gesture detected: " + action.lower() )
    engine.runAndWait()

def bind(action):
    key = search_keys(action.lower())
    
    # notification toast 
    # notify(action)

    # sound notification
    sound_notification(action)

    keyboard.press_and_release(key)