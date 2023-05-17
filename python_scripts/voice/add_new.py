import sys
import os
from database import write_keys

dirname = os.path.dirname(__file__)
parent = os.path.dirname(dirname)
main_dir = os.path.dirname(parent)

def write_action():
    speech_file = os.path.join(main_dir, 'Electron/gestureFile/file.txt')
    f=open(speech_file,"r")
    action=f.readline()
    keys=f.readline()
    print(action[:-1],keys)
    write_keys(action[:-1],keys)
    
if (sys.argv[1] == 'train'):
    write_action()