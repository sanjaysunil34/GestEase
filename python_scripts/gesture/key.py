import keyboard
from time import sleep
import time
from functionality import openapp, sing,search_for


def bind(action):
    check = 1

    if(action == 'play' or action == 'pause'):
        keyboard.press('space')
    elif(action == 'increase volume'):
        keyboard.press('up')
    elif(action == 'decrease volume'):
        keyboard.press('down')
    elif(action == 'go back' or action == 'previous'):
        keyboard.press('left')
    elif(action == 'go forward' or action == 'next'):
        keyboard.press('right')
    elif(action == 'full screen' or action == 'exit full screen'):
        keyboard.press('f')
    elif(action == 'present'):
        keyboard.press('F5')
    elif(action == 'ok'):
        keyboard.press('enter')
    elif(action == 'mute'):
        keyboard.press('m')
    elif(action == 'down'):
        keyboard.press_and_release('tab')
    elif(action == 'ok'):
        keyboard.press_and_release('enter')
    elif(action == 'close'):
        keyboard.press('c')
    elif("open app" in action.lower()):
        openapp(action)
    elif("sing" in action.lower()):
        openapp('open app chrome')
        sing(action)
    elif("search for" in action.lower()):
        search_for(action)

    if(not check):
        time.sleep(2)
