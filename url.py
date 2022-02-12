from fastapi import FastAPI, HTTPException

from status import get_status
app = FastAPI()

@app.get("/status/{room}")
def get_status(room:str):
    return get_status(room)

@app.get("/status/all}")
def get_all_status():
    return get_all_status()