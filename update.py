from datetime import datetime
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

client = MongoClient('mongodb://localhost:27017/')

mydb = client["Light"]
collection = mydb["status"]

app = FastAPI()

class ss(BaseModel):
    room : str
    status : int

def del1():
    for x in collection.find():
        print(x)

def i_log1(inn,out):
    collection1 = mydb["log1"]
    c2 = {"inn": inn , "out": out}
    x = collection1.insert_one(c2)

def i_log2(inn,out):
    collection2 = mydb["log2"]
    c2 = {"inn": inn, "out": out}
    x = collection2.insert_one(c2)

def i_log3(inn,out):
    collection3 = mydb["log3"]
    c2 = {"inn": inn , "out": out}
    x = collection3.insert_one(c2)

def update(ms: ss):
    nt = datetime.now()
    now_time = datetime.timestamp(nt)
    if(ms.status == 1):
        my_query = {"room":ms.room}
        new_query = {"$set": {"status":int(ms.status),"first": now_time,"last":None}}
        collection.update_one(my_query,new_query)
    if (ms.status == 0):
        my_query = {"room": ms.room}
        new_query = {"$set": {"status": int(ms.status), "last":now_time}}
        collection.update_one(my_query, new_query)

        result = collection.find({"room":ms.room})
        result = list(result)
        if len(result) == 0:
            return {
                "status": "room not found"
            }
        x = result[0]
        #Insert to log
        if (ms.room == 'l1'):
           i_log1(x['first'],x['last'])
        if (ms.room == 'l2'):
           i_log2(x['first'],x['last'])
        if (ms.room == 'l3'):
           i_log3(x['first'],x['last'])
        
