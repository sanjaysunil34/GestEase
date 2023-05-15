import os
import sys
from tinydb import TinyDB, Query

dirname = os.path.dirname(__file__)
parent = os.path.dirname(dirname)
main_dir = os.path.dirname(parent)
db_path = os.path.join(os.getcwd())
path_str = db_path.split('electron')
print(path_str[0])
new = path_str[0]+'\python_scripts\\voice\db.json'
# print(new)

db = TinyDB(new)
act = Query()
actions_list=[]

def list_actions():
    for item in db:
        actions_list.append(item['action'])
    return actions_list

def write_keys(action,keys):
    db.insert({'action': action.lower(), 'keys': keys})
    
def search_keys(action):
    temp=db.search(act.action==action)
    print(temp)
    sys.stdout.flush()
    if temp:
        temp1=temp[0]
        return temp1['keys']
