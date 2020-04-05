from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic!"}

class MethodResp(BaseModel):
    method: str

@app.get('/{method}', response_model=MethodResp) #dynamiczne adresy
def print_method(method: str):
    return MethodResp(method=f"{method}")
