import speech_recognition as sr
from datetime import datetime
from key import bind
import sys
from database import list_actions

keywords=list_actions()


def Main():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print(datetime.now().time(), " Listening....")
            audio = r.listen(source)
            print(datetime.now().time(), " Recognizing....")
            r.adjust_for_ambient_noise(source)
            text = r.recognize(audio)
            print(text)
            print(datetime.now().time(), "Text : ", text.lower())

            if len(text) == 0:
                Main()
            elif "open app" in text.lower() or "search for" in text.lower():
                print('Executing ', text)
                bind(text)
            else:
                for key in keywords:
                    if key in text.lower():
                        print('Executing ', key)
                        bind(key)
                        break
            Main()
    except Exception as e:
        Main()
        print(e)
# Main()

command = sys.argv[1]

if command == "start":
    Main()
    sys.stdout.flush()
