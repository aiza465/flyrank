from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

tasks = [
    {
        "id":1,
        "title":"Study",
        "done":False
    },
    {
        "id":2,
        "title":"Sleep",
        "done":True
    },
    {
        "id":3,
        "title":"Workout",
        "done":False
    }
]
class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.get("/tasks/{id}")
async def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    else :
        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task

@app.put("/tasks/{id}")
def update_task(id: int, upd_task: TaskUpdate):

    for task in tasks:

        if task["id"] == id:

            if upd_task.title is None and upd_task.done is None:
                raise HTTPException(
                    status_code=400,
                    detail="Request body cannot be empty"
                )

            if upd_task.title is not None:
                if upd_task.title.strip() == "":
                    raise HTTPException(
                        status_code=400,
                        detail="Title cannot be empty"
                    )
                task["title"] = upd_task.title

            if upd_task.done is not None:
                task["done"] = upd_task.done

            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

