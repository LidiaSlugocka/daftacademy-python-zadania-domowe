from fastapi.testclient import TestClient
from main import app, PatientBasicData
import pytest

client = TestClient(app)
client.id = -1
client.patients = dict()

# Test zadania 1
def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World during the coronavirus pandemic!"}

# Test zadania 2
def test_get_method():
    response = client.get("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "GET"}

def test_post_method():
    response = client.post("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "POST"}

def test_put_method():
    response = client.put("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "PUT"}

def test_delete_method():
    response = client.delete("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "DELETE"}

# Test zadania 3
@pytest.mark.parametrize("my_patient", [{"name": "Lidia", "surename": "Slugocka"}, {"name": "Barack", "surename": "Obama"}])
def test_new_patient(my_patient):
    response = client.post("/patient", json=my_patient)
    client.id += 1
    client.patients[client.id] = my_patient
    assert response.status_code == 200
    assert response.json() == {"id": client.id, "patient": my_patient}

# Test zadania 4
#@pytest.mark.parametrize()
#def test_find_patient(pk):
#    response = client.get("/patient/{pk}")
#    assert response.status_code == 200
    
    