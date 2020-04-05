from typing import Dict

from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()


# Zadanie 1
@app.get("/")
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic!"}

# Zadanie 2
#class GiveMeSomethingRq(BaseModel):
#    first_key: str


class GiveMeSomethingResp(BaseModel):
    method: str
    #received: Dict
    #constant_data: str = "python jest super"

@app.get("/{method}", response_model=GiveMeSomethingResp)
def receive_something(method: str):
    return GiveMeSomethingResp(method=f'{method}')

@app.post("/{method}", response_model=GiveMeSomethingResp)
def receive_something(method: str):
    return GiveMeSomethingResp(method=f'{method}')