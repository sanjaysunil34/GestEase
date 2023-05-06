import os
from tinydb import TinyDB, Query
dirname = os.path.dirname(__file__)
parent = os.path.dirname(dirname)
main_dir = os.path.dirname(parent)
db_path = os.path.join(os.getcwd())
path_str=db_path.split('Electron')
new=path_str[0]+'/python_scripts/gesture/db.json'
db = TinyDB(new)
act=Query()


gesture_file = os.path.join(main_dir, 'Electron/gestureFile/manual.txt')
f=open(gesture_file,"w")
for item in db:
    str=''
    str=item['action']+' '+item['keys']+' '+item['image']+'\n'
    print(str)
    f.writelines(str)