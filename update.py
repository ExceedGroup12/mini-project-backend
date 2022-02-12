import json
import time
from fastapi import FastAPI, HTTPException
from bson import json_util
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

client = MongoClient('mongodb://localhost:27017/')

mydb = client["Light"]
collection = mydb["status"]

app = FastAPI()

class ss(BaseModel):
    room : str
    status : int

def i_log1(time,in_out):
    collection1 = mydb["log1"]
    c2 = {"time": time, "ss": in_out}
    x = collection1.insert_one(c2)

def i_log2(time,in_out):
    collection2 = mydb["log2"]
    c2 = {"time": time, "ss": in_out}
    x = collection2.insert_one(c2)

def i_log3(time,in_out):
    collection3 = mydb["log3"]
    c2 = {"time": time, "ss": in_out}
    x = collection3.insert_one(c2)

@app.put("/update")
def update(ms: ss):
    now_time = time.time()
    if(ms.status == 1):
        my_query = {"room":ms.room}
        new_query = {"$set": {"status":int(ms.status),"first": now_time,"last":None}}
        collection.update_one(my_query,new_query)
    if (ms.status == 0):
        my_query = {"room": ms.room}
        new_query = {"$set": {"status": int(ms.status), "last":now_time}}
        collection.update_one(my_query, new_query)
    #Insert to log
    if (ms.room == 'l1'):
        i_log1(now_time, ms.status)
    if (ms.room == 'l2'):
        i_log2(now_time, ms.status)
    if (ms.room == 'l3'):
        i_log3(now_time, ms.status)
