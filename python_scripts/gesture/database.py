import os
from tinydb import TinyDB, Query
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
    db.insert({'action': action, 'keys': keys})

def search_keys(action):
    temp=db.search(act.action==action)
    # print("action",temp[0]['action']," key: ",temp[0]['keys'])
    if temp:
        temp1=temp[0]
        return temp1['keys']




