from tinydb import TinyDB, Query
db = TinyDB('db.json')
act=Query()
def write_keys(action,keys):
    db.insert({'action': action, 'keys': keys})

def search_keys(action):
    temp=db.search(act.action==action)
    print(temp)
    if temp:
        temp1=temp[0]
        return temp1['keys']