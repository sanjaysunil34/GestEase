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
    for i in word.lower():
        print(i)
        keyboard.press_and_release(i)
    time.sleep(1)
    keyboard.send('enter')


def sing(action):
    time.sleep(10)
    app = action.split()
    arr = list(app[1:])
    word = ""
    for i in arr:
        word = word + " " + i
    print(word)
    time.sleep(1)
    keyboard.send('down')
    keyboard.press_and_release('/')
    time.sleep(1)
    for i in word.lower():
        print(i)
        keyboard.press_and_release(i)
    time.sleep(1)
    keyboard.send('enter')
    time.sleep(3)
    keyboard.press_and_release('tab')
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
