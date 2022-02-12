from fastapi import FastAPI, HTTPException
from status import get_all_data, get_data
import status

app = FastAPI()

@app.get("/status/{room}")
def get_status(room:str):
    return get_data(room)

@app.get("/allStatus")
def get_all_status():
    return get_all_data()