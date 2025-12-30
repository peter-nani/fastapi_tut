import os
import tempfile
import json
from sqlmodel import create_engine, SQLModel, Session
from fastapi.testclient import TestClient

from app.main import app
from app.db import get_session
from app import models


def setup_module(module):
    # Use a temporary sqlite file for tests
    module.db_fd, module.db_path = tempfile.mkstemp(suffix=".db")
    module.test_db_url = f"sqlite:///{module.db_path}"
    module.test_engine = create_engine(module.test_db_url, echo=False)
    SQLModel.metadata.create_all(module.test_engine)


def teardown_module(module):
    try:
        os.close(module.db_fd)
        os.remove(module.db_path)
    except Exception:
        pass


def get_test_session():
    with Session(test_engine) as session:
        yield session


app.dependency_overrides[get_session] = get_test_session
client = TestClient(app)


def test_create_and_list_user():
    payload = {"name": "Tester", "email": "tester@example.com", "password": "x"}
    r = client.post("/api/v1/users/", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == "Tester"

    r2 = client.get("/api/v1/users/")
    assert r2.status_code == 200
    arr = r2.json()
    assert isinstance(arr, list)
    assert any(u["email"] == "tester@example.com" for u in arr)
