# import speech_recognition as sr
# from datetime import datetime
# from key import bind
# import sys


# def Main():
#     r = sr.Recognizer()
#     try:
#         with sr.Microphone() as source:
#             print("Time : ", datetime.now().time())
#             print("Listening....")
#             audio = r.listen(source)
#             print("Time : ", datetime.now().time())
#             print("Recognizing....")
#             r.adjust_for_ambient_noise(source)
#             text = r.recognize(audio)
#             print("Time : ", datetime.now().time())
#             print(text.lower())
#             if len(text) == 0:
#                 Main()
#             elif "play" in text.lower():
#                 print('playing')
#                 bind('play')
#             elif "pause" in text.lower():
#                 print('pausing')
#                 bind('pause')
#             elif "increase volume" in text.lower():
#                 print('increasing volume')
#                 bind('increase volume')
#             elif "decrease volume" in text.lower():
#                 print('decreasing volume')
#                 bind('decrease volume')
#             elif "full screen" in text.lower():
#                 print('full screen')
#                 bind('full screen')
#             elif "exit full screen" in text.lower():
#                 print('exiting full screen')
#                 bind('full screen')
#             elif "mute" in text.lower() or "unmute" in text.lower():
#                 print('mute')
#                 bind('mute')
#             elif "close" in text.lower():
#                 print('close')
#                 bind('close')
#             elif "go back" in text.lower():
#                 print('go back')
#                 bind('go back')
#             elif "forward" in text.lower():
#                 print('go forward')
#                 bind('go forward')
#             elif "open app" in text.lower():
#                 print(text)
#                 bind(text)
#             elif "sing" in text.lower():
#                 print(text)
#                 bind(text)
#             elif "search for" in text.lower():
#                 print(text)
#                 bind(text)

#             Main()
#     except Exception as e:
#         Main()
#         print(e)


# command = sys.argv[1]
# print(command)
# if command == "start":
#     Main()
#     sys.stdout.flush()
# # Main()


import speech_recognition as sr
from datetime import datetime
from key import bind
import sys

keywords = ['play', 'pause', 'increase volume', 'decrease volume', 'full screen', 'exit full sreen', 'mute', 'close',
            'go back', 'forward', 'sing', 'present', 'down', 'next', 'previous', 'ok']


def Main():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print(datetime.now().time(), " Listening....")
            audio = r.listen(source)
            print(datetime.now().time(), " Recognizing....")
            r.adjust_for_ambient_noise(source)
            text = r.recognize(audio)
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


command = sys.argv[1]

if command == "start":
    Main()
    sys.stdout.flush()
