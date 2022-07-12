import keyboard
import time

def openapp(action):
    app = action.split()
    print(app)
    arr = list(app[2:])
    word = ""
    for i in arr:
        word = word+" "+i
    print(word)
    keyboard.press_and_release('windows')
    time.sleep(1)
    for i in word:
        print(i)
        keyboard.press_and_release(i) 

    time.sleep(1)
    keyboard.send('enter')

def search_for(action):
    app = action.split()
    print(app)
    arr = list(app[2:])
    word = ""
    for i in arr:
        word = word+" "+i
    print(word)
    keyboard.send('ctrl+l')
    time.sleep(1)
    for i in word:
        print(i)
        keyboard.press_and_release(i) 

    time.sleep(1)
    keyboard.send('enter')