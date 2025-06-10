import pytest
from flask_openapi3 import OpenAPI, Info
from main import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client


def test_post_user_success(client):
    res = client.post('/api/user', json={"name": "testuser", "age": 22, "optional_field": None}, query_string={"param1": "testuser", "param2": 22})
    assert res.status_code == 200
    assert res.json["name"] == "testuser"
    assert res.json["age"] == 22

def test_post_user_notfound(client):
    res = client.post('/api/user', json={"name": "bodyuser", "age": 22, "optional_field": None}, query_string={"param1": "bodyuser", "param2": 22})
    assert res.status_code == 200
    assert res.json["name"] == "bodyuser"

def test_post_user_validation(client):
    res = client.post('/api/user', json={"name": "a", "age": 0, "optional_field": None}, query_string={"param1": "a", "param2": 0})
    assert res.status_code == 422

def test_post_user_query_overrides_body(client):
    # クエリパラメータがbodyより優先される
    res = client.post('/api/user', json={"name": "bodyuser", "age": 22, "optional_field": None}, query_string={"param1": "queryuser", "param2": 33})
    assert res.status_code == 200
    assert res.json["name"] == "queryuser"
    assert res.json["age"] == 33

def test_post_user_notfound_query(client):
    # param1が"notfound"なら404
    res = client.post('/api/user', json={"name": "bodyuser", "age": 22, "optional_field": None}, query_string={"param1": "notfound", "param2": 22})
    assert res.status_code == 404
    assert "error" in res.json
