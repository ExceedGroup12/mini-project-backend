from pymongo import MongoClient
import time

client = MongoClient('mongodb://localhost', 27017)

db = client["Light"]
menu_collection = db["status"]

def get_data(room:str):
    r = menu_collection.find({"room":room})
    diff = compute_diff_time(r["first"], r["last"])
    return{
        "room":room,
        "status":r["status"],
        "diff": diff
    }
    
def compute_diff_time(first, last):
    if first == None:
        diff = None
    elif last == None:
        diff = time.time() - first
    else:
        diff = last - first
    return diff
    
def get_all_data():
    data = []
    r = menu_collection.find()
    for rooms in r:
        print(rooms)
        data.append({
            "room":rooms["room"],
            "status":rooms["status"],
            "diff": compute_diff_time(rooms["first"], rooms["last"])
        })
    return data

def compute_estimate_time():
    r = get_all_data()
    
    
print(get_all_data())