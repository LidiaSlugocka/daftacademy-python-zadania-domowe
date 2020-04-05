from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# Zadanie 1
@app.get("/")
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic!"}

# Zadanie 2
class MethodResp(BaseModel):
    method: str

@app.get('/{method}', response_model=MethodResp)
def print_method(method: str):
    return MethodResp(method=f"{method}")

@app.post('/{method}', response_model=MethodResp)
def print_method(method: str):
    return MethodResp(method=f"{method}")

@app.put('/{method}', response_model=MethodResp)
def print_method(method: str):
    return MethodResp(method=f"{method}")

@app.delete('/{method}', response_model=MethodResp)
def print_method(method: str):
    return MethodResp(method=f"{method}")
