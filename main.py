from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
app.counter = -1

# Zadanie 1
@app.get("/")
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic!"}

# Zadanie 2
class MethodReturn(BaseModel):
    method: str

@app.get("/method", response_model=MethodReturn)
def get_method():
    return MethodReturn(method='GET')

@app.post("/method", response_model=MethodReturn)
def post_method():
    return MethodReturn(method='POST')

@app.put("/method", response_model=MethodReturn)
def put_method():
    return MethodReturn(method='PUT')

@app.delete("/method", response_model=MethodReturn)
def delete_method():
    return MethodReturn(method='DELETE')

# Zadanie 3
class PatientBasicData(BaseModel):
    name: str
    surname: str

class PatientData(BaseModel):
    id: int
    patient: PatientBasicData
    
@app.post("/patient", response_model=PatientData)
def new_patient(patientData: PatientBasicData):
    app.counter += 1
    return PatientData(id=app.counter, patient=patientData)

# Zadanie 4
