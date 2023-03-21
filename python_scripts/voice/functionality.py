import keyboard
import time

def openapp(action):
    app = action.split()
    #print(app)
    arr = list(app[2:])
    word = ""
    for i in arr:
        word = word+" "+i
    #print(word)
    keyboard.press_and_release('windows')
    time.sleep(1)
    for i in word.lower():
        #print(i)
        keyboard.press_and_release(i)
    time.sleep(1)
    keyboard.send('enter')


def sing(action):
    time.sleep(1)
    keyboard.send('ctrl+l')
    time.sleep(3)
    word = "https://www.youtube.com/results?search_query="
    for i in word.lower():
        #print(i)
        if(i == '_'):
            keyboard.press_and_release('shift+_')
        elif(i == '?'):
            keyboard.press_and_release('shift+?')
        else:
            keyboard.press_and_release(i)
    time.sleep(1)
    app = action.split()
    arr = list(app[1:])
    word = ""
    for i in arr:
        word = word + i + " "
    word = word[:-1]
    #print(word)
    time.sleep(1)
    for i in word.lower():
        #print(i)
        keyboard.press_and_release(i)
    time.sleep(3)
    keyboard.send('enter')
    time.sleep(3)
    keyboard.press_and_release('tab')
    keyboard.send('enter')


def search_for(action):
    app = action.split()
    #print(app)
    arr = list(app[2:])
    word = ""
    for i in arr:
        word = word+" "+i
    #print(word)
    keyboard.send('ctrl+l')
    time.sleep(1)
    for i in word:
        #print(i)
        keyboard.press_and_release(i)

    time.sleep(1)
    keyboard.send('enter')
