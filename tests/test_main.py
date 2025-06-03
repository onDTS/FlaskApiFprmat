import pytest
from flask_openapi3 import OpenAPI, Info
from main import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_post_user_success(client):
    res = client.post('/api/user', json={"name": "testuser", "age": 22})
    assert res.status_code == 200
    assert res.json["name"] == "testuser"
    assert res.json["age"] == 22

def test_post_user_notfound(client):
    res = client.post('/api/user', json={"name": "notfound", "age": 22})
    assert res.status_code == 404
    assert "error" in res.json

def test_post_user_validation(client):
    res = client.post('/api/user', json={"name": "a", "age": 0})
    assert res.status_code == 422
