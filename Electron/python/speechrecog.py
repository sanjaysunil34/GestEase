import speech_recognition as sr
from datetime import datetime
import sys


def Main():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Time : ", datetime.now().time())
            print("Listening....")
            audio = r.listen(source)
            print("Time : ", datetime.now().time())
            print("Recognizing....")
            r.adjust_for_ambient_noise(source)
            text = r.recognize(audio)
            print("Time : ", datetime.now().time())
            print(text.lower())
            if len(text) == 0:
                Main()
            elif "play" in text.lower():
                print('plaaying')
                Main()
            elif "pause" in text.lower():
                print('pausing')
                Main()
            print('blah')
            Main()
    except Exception as e:
        Main()
        print(e)


command = sys.argv[1]
if command == "start":
    Main()
    sys.stdout.flush()

# Main()
