import os
from tinydb import TinyDB, Query
dirname = os.path.dirname(__file__)
parent = os.path.dirname(dirname)
main_dir = os.path.dirname(parent)
db_path = os.path.join(os.getcwd())
path_str=db_path.split('Electron')
new=path_str[0]+'python_scripts/gesture/db.json'
# print(new)

db = TinyDB(new)
act=Query()

actions_list=[]
# for item in db:
#         print(item['action'])

def list_actions():
    for item in db:
        actions_list.append(item['action'])
    # print(actions_list)
    return actions_list
def write_keys(action,keys):
    image = action + '.jpg'
    db.insert({'action': action, 'keys': keys, 'image': image})
    write_to_manual()

def write_to_manual():
    gesture_file = os.path.join(main_dir, 'Electron/gestureFile/manual.txt')
    f=open(gesture_file,"w")
    for item in db:
        str=''
        str=item['action']+' '+item['keys']+' '+item['image']+'\n'
        print(str)
        f.writelines(str)

def search_keys(action):
    temp=db.search(act.action==action)
    # print(temp)
    if temp:
        temp1=temp[0]
        return temp1['keys']




