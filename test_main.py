from fastapi.testclient import TestClient

import main
from main import app

client = TestClient(app)


def setup_function():
    main.tasks.clear()
    main.next_id = 1


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_index_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "TODO List" in response.text


def test_initial_tasks_empty():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_add_task():
    new_task = {"title": "Test Task"}
    response = client.post("/tasks", json=new_task)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == new_task["title"]


def test_tasks_after_add():
    client.post("/tasks", json={"title": "Task 1"})
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1


def test_delete_task():
    client.post("/tasks", json={"title": "To delete"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    msg = response.json()
    assert "deleted" in msg["message"]


def test_delete_not_found():
    response = client.delete("/tasks/9999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
