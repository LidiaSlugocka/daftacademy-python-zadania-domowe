from typing import Dict

from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()


# Zadanie 1
@app.get("/")
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic!"}

# Zadanie 2
class MethodReturn(BaseModel):
    method: str

@app.get("/{method}", response_model=MethodReturn)
def get_method(method: str):
    return MethodReturn(method='GET')

@app.post("/{method}", response_model=MethodReturn)
def post_method(method: str):
    return MethodReturn(method='POST')

@app.put("/{method}", response_model=MethodReturn)
def put_method(method: str):
    return MethodReturn(method='PUT')

@app.delete("/{method}", response_model=MethodReturn)
def delete_method(method: str):
    return MethodReturn(method='DELETE')