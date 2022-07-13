import speech_recognition as sr
from datetime import datetime
from key import bind
import sys
from constants import keywords 

def Main(): 
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Time : ",datetime.now().time())
            print("Listening....")
            audio = r.listen(source)
            print("Time : ",datetime.now().time())
            print("Recognizing....")
            r.adjust_for_ambient_noise(source)
            text = r.recognize(audio)
            print("Time : ",datetime.now().time())
            print(text.lower())
            if len(text) == 0:
                Main()
            elif "open app" in text.lower() or  "search for" in text.lower():
                print(text)
                bind(text)
            else:
                for key in keywords:
                    if key in text.lower():
                        print(key)
                        bind(key)
                        break
            Main()
    except Exception as e:
        Main()
        print(e)

command = sys.argv[1]
print(command)
if command == "start":
    Main()
    sys.stdout.flush()
# Main()