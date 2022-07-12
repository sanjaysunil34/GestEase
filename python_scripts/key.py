import keyboard
from time import sleep
from functionality import openapp

def bind(action):
    check = 1

    if(action=='play'or action=='pause'):
        keyboard.press('space')
    elif(action=='increase volume'):
        keyboard.press('up')
    elif(action=='go back'):
        keyboard.press('left')
    elif(action=='go forward'):
        keyboard.press('right')
    elif(action=='decrease volume'):
        keyboard.press('down')        
    elif(action=='full screen' or action=='exit full screen'):
        keyboard.press('f')    
    elif(action=='mute'):
        keyboard.press('m')  
    elif(action=='close'):
        keyboard.send('alt+F4')
    elif("open app" in action.lower()):
        openapp(action)
    elif("search for" in action.lower()):
        search_for(action)

    if(not check):
        time.sleep(2)


