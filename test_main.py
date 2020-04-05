from fastapi.testclient import TestClient

from main import app

import pytest

client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World during the coronavirus pandemic!"}

@pytest.mark.parametrize("method", ['Zenek', 'Marek', 'Ziemniak'])
def test_get_method(method):
    response = client.get(f"/{method}")
    assert response.status_code == 200
    assert response.json() == {"method": "GET"}

@pytest.mark.parametrize("method", ['Zenek', 'Marek', 'Ziemniak'])
def test_post_method(method):
    response = client.post(f"/{method}")
    assert response.status_code == 200
    assert response.json() == {"method": "POST"}

@pytest.mark.parametrize("method", ['Zenek', 'Marek', 'Ziemniak'])
def test_put_method(method):
    response = client.put(f"/{method}")
    assert response.status_code == 200
    assert response.json() == {"method": "PUT"}

@pytest.mark.parametrize("method", ['Zenek', 'Marek', 'Ziemniak'])
def test_delete_method(method):
    response = client.delete(f"/{method}")
    assert response.status_code == 200
    assert response.json() == {"method": "DELETE"}