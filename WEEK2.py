from fastapi import FastAPI, HTTPException

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

