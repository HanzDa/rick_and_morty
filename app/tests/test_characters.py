from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_characters_from_external_service():
    response = client.get('/api/characters')
    assert response.status_code == 200


def test_get_characters_from_db():
    response = client.get('/api/characters/1')
    assert response.status_code == 200


def test_create_new_characters_from_service():
    response = client.post('/api/characters')
    assert response.status_code == 201
    assert response.json() == "0 new characters were created"
