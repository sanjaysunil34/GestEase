import keyboard
from time import sleep
import time
from functionality import openapp, sing,search_for


def bind(action):
    print(action)
    if(action == 'Play/Pause'):
        keyboard.press('space')
    elif(action == 'Increase'):
        keyboard.press('up')
    elif(action == 'Decrease'):
        keyboard.press('down')
    elif(action == 'Previous'):
        keyboard.press('left')
    elif(action == 'Next'):
        keyboard.press('right')
    elif(action == 'Ok'):
        keyboard.press_and_release('enter')
    elif(action == 'Close'):
        keyboard.press_and_release('alt+F4')
    elif(action == 'Switch'):
        keyboard.press_and_release('win + tab')
    elif(action == 'Present'):
        keyboard.press('F5')
    elif(action == 'End_Present'):
        keyboard.press('esc')
    sleep(2)
    # elif(action == 'full screen' or action == 'exit full screen'):
    #     keyboard.press('f')
    # elif(action == 'present'):
    #     keyboard.press('F5')
    # elif(action == 'ok'):
    #     keyboard.press('enter')
    # elif(action == 'mute'):
    #     keyboard.press('m')
    # elif(action == 'down'):
    #     keyboard.press_and_release('tab')
    # elif("open app" in action.lower()):
    #     openapp(action)
    # elif("sing" in action.lower()):
    #     openapp('open app chrome')
    #     sing(action)
    # elif("search for" in action.lower()):
    #     search_for(action)

    # if(not check):
    #     time.sleep(2)
