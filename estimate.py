import json
from unittest import result
from fastapi import FastAPI, HTTPException
from bson import json_util
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

client = MongoClient('mongodb://localhost:27017/')

mydb = client["Light"]

collection1 = mydb["log1"]
collection2 = mydb["log2"]
collection3 = mydb["log3"]

def calculate_estimate():
    result1 = collection1.find({}, {"_id":0})
    result2 = collection2.find({}, {"_id":0})
    result3 = collection3.find({}, {"_id":0})
    all_result = list(result1) + list(result2) + list(result3)
    diff_list = [log["out"] - log["inn"] for log in all_result]
    return sum(diff_list)/len(diff_list)