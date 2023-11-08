import unittest

from fastapi.testclient import TestClient
from pydantic_core import ValidationError

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.base import Base
from app.database.session import get_db
from app.schemas.characters import Character
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


class TestCase(unittest.TestCase):
    def test_create_new_characters_from_service(self):
        response = client.get('/api/characters/1')
        assert response.status_code == 404
        assert response.json() == {"detail": "Character with id 1 not found"}

        response = client.post('/api/characters?page=1')
        assert response.status_code == 201
        assert "new characters were created" in response.json()

    def test_get_characters_from_external_service(self):
        response = client.get('/api/characters')
        assert response.status_code == 200

    def test_get_characters_from_db(self):
        response = client.get('/api/characters/1')
        assert response.status_code == 200
        data = response.json()
        assert type(data) is dict
        try:
            data['name'] = 5
            Character(**data)
        except ValidationError as e:
            assert e.error_count() == 1
