import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
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

def test_create_user():
    response = client.post(
        "/users/",
        json={"username": "testuser2", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser2"

def test_login():
    response = client.post(
        "/auth/token",
        data={"username": "testuser2", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_movie():
    response = client.post(
        "/auth/token",
        data={"username": "testuser2", "password": "testpassword"}
    )
    token = response.json()["access_token"]

    response = client.post(
        "/movies/",
        json={"title": "Inception", "description": "A mind-bending thriller by Christopher Nolan."},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Inception"

def test_read_movies():
    response = client.get("/movies/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_read_movie():
    response = client.get("/movies/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Inception"


def test_create_rating():
    response = client.post(
        "/auth/token",
        data={"username": "testuser2", "password": "testpassword"}
    )
    token = response.json()["access_token"]

    response = client.post(
        "/movies/1/ratings/",
        json={"rating": 4.5},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["rating"] == 4.5

def test_read_ratings():
    response = client.get("/movies/1/ratings/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_comment():
    response = client.post(
        "/auth/token",
        data={"username": "testuser2", "password": "testpassword"}
    )
    token = response.json()["access_token"]

    response = client.post(
        "/movies/1/comments/",
        json={"content": "Great movie!"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["content"] == "Great movie!"

def test_read_comments():
    response = client.get("/movies/1/comments/")
    assert response.status_code == 200
    assert len(response.json()) > 0
