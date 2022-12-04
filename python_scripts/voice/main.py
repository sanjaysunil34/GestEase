import speech_recognition as sr
from datetime import datetime
from key import bind
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
                bind('play')
                Main()
            elif "pause" in text.lower():
                print('pausing')
                bind('pause')
                Main()
            elif "increase" in text.lower():
                print('increase')
                bind('increase')
                Main()
            elif "present" in text.lower():
                print('present')
                bind('present')
                Main()
            elif "next" in text.lower():
                print('next')
                bind('next')
                Main()
            elif "previous" in text.lower():
                print('previous')
                bind('previous')
                Main()
            elif "escape" in text.lower():
                print('escape')
                bind('escape')
                Main()
            elif "windows" in text.lower():
                print('windows')
                bind('windows')
                Main()
            # elif "powerpoint" in text.lower():
            #     print('powerpoint')
            #     bind('powerpoint')
            #     Main()
            elif "ok" in text.lower():
                print('ok')
                bind('ok')
                Main()
            elif "down" in text.lower():
                print('down')
                bind('down')
                Main()
            elif "close" in text.lower():
                print('close')
                bind('close')
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
