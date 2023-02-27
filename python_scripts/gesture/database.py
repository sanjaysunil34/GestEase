from tinydb import TinyDB, Query
db = TinyDB('C:/Users/Hp/OneDrive/Documents/GitHub/GestEase/python_scripts/gesture/db.json')
act=Query()

actions_list=[]

def list_actions():
    for item in db:
        actions_list.append(item['action'])
    # print(actions_list)
    return actions_list
def write_keys(action,keys):
    db.insert({'action': action, 'keys': keys})

def search_keys(action):
    temp=db.search(act.action==action)
    print(temp)
    if temp:
        temp1=temp[0]
        return temp1['keys']




