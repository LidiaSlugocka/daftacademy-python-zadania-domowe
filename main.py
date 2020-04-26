from fastapi import FastAPI, Response, HTTPException, Depends, Cookie, status
from pydantic import BaseModel
from hashlib import sha256
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import RedirectResponse

import secrets

app = FastAPI()
app.counter = -1
app.patients = dict()

# Zadanie 1
@app.get("/")
@app.get("/welcome")
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
    surename: str

class PatientData(BaseModel):
    id: int
    patient: PatientBasicData
    
@app.post("/patient", response_model=PatientData)
def new_patient(patient_data: PatientBasicData):
    app.counter += 1
    app.patients[app.counter] = patient_data
    return PatientData(id=app.counter, patient=patient_data)

# Zadanie 4
@app.get("/patient/{pk}", response_model=PatientBasicData)
def find_patient(pk: int):
    if pk in app.patients.keys():
        return app.patients[pk]
    else:
        raise HTTPException(204,"No such patient!")

############################################################################ F_jak_ficzur
# Zadanie 2
my_user = {"trudnY": "paC13Nt"}
app.secret_key = "it is only my secret key and noone knows it"
app.tokens = []
security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    my_username = secrets.compare_digest(credentials.username, "trudnY")
    my_password = secrets.compare_digest(credentials.password, "paC13Nt")
    if my_username and my_password:
        session_token = sha256(bytes(f"{user}{password}{app.secret}", encoding="utf8")).hexdigest()
        app.tokens += session_token
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return credentials.username

@app.post("/login")
def log_into(response: Response, user_credentials = Depends(get_current_user)):
        response.set_cookie(key="session_token", value=session_token)
        response = RedirectResponse(url="/welcome")
        return response