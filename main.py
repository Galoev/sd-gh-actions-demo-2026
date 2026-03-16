from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

tasks = []
next_id = 1

BASE_DIR = Path(__file__).parent


class TaskCreate(BaseModel):
    title: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def read_index():
    content = (BASE_DIR / "index.html").read_text(encoding="utf-8")
    return content


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def add_task(task: TaskCreate):
    global next_id
    new_task = {
        "id": next_id,
        "title": task.title
    }
    tasks.append(new_task)
    next_id += 1
    return new_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for existing_task in tasks:
        if existing_task["id"] == task_id:
            tasks.remove(existing_task)
            return {"message": f"Task {task_id} deleted"}
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
