from pymongo import MongoClient
from datetime import datetime



from estimate import calculate_estimate


client = MongoClient('mongodb://localhost', 27017)

db = client["Light"]
menu_collection = db["status"]

def get_data(room:str):
    r = menu_collection.find({"room":room})
    r = list(r)
    if len(r) == 0:
        return {
        "room":None,
        "status":"Not Found",
        "diff": None
        }
    now = datetime.now()
    estimate_time = r[0]["first"] + calculate_estimate() - datetime.timestamp(now)
    if estimate_time < 0:
        estimate_time = "Over estimate"
    diff = compute_diff_time(r[0]["first"], r[0]["last"])
    dt_object = datetime.fromtimestamp(r[0]["first"])
    return{
        "room":room,
        "status":r[0]["status"],
        "diff": diff,
        "first": dt_object,
        "estimate": estimate_time
    }
    
def compute_diff_time(first, last):
    if first != None and last == None:
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        diff = timestamp - first
    else:
        diff = None
    return diff
    
def get_all_data():
    data = []
    r = menu_collection.find()
    for rooms in r:
        dt_object = datetime.fromtimestamp(rooms["first"])
        data.append({
            "room":rooms["room"],
            "status":rooms["status"],
            "diff": compute_diff_time(rooms["first"], rooms["last"]),
            "first": dt_object,
        })
    return data


