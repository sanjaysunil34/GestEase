import keyboard
import time
time.sleep(3)
word = "https://www.youtube.com/results?search_query=hello"
for i in word.lower():
    print(i)
    if(i=='_'):
        keyboard.press_and_release('shift+_')
    else:
        keyboard.press_and_release(i)
time.sleep(1)


