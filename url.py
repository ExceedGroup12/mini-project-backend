from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from status import get_all_data, get_data
from estimate import calculate_estimate
from update import update, ss

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status/{room}")
def get_status(room:str):
    return get_data(room)

@app.get("/allStatus")
def get_all_status():
    return get_all_data()

@app.post("/update")
def update_data(ms: ss):
    return update(ms)