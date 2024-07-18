from datetime import datetime
import os
from bson import ObjectId
import bson
from fastapi import FastAPI, HTTPException, status
from dotenv import load_dotenv
from motor import motor_asyncio
from pydantic import BaseModel
from pymongo import ReturnDocument

from models.task import Task
# from models.user import User

load_dotenv()

client = motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.get_database("task_manager")
user_collection = db.get_collection("users")
task_collection = db.get_collection("tasks")


app = FastAPI()

"""
TODO: Create Users Endpoints

POST /users: Create a new user.
GET /users/{user_id}: Get details of a specific user.
PUT /users/{user_id}: Update user information.
DELETE /users/{user_id}: Delete a user.
"""




"""
TODO: Tasks Endpoints

POST /users/{user_id}/tasks: Create a new task for a user.
GET /users/{user_id}/tasks/{task_id}: Get details of a specific task for a user.
GET /users/{user_id}/tasks: List all tasks for a user.
PUT /users/{user_id}/tasks/{task_id}: Update task information for a user.
DELETE /users/{user_id}/tasks/{task_id}: Delete a task for a user.
"""


class TaskEdit(BaseModel):
    """This is required when editing task"""
    title: str | None = None
    description: str | None = None
    status: str | None = None

@app.get("/tasks", response_model=list[Task])
async def fetch_tasks():
    """Fetches all the tasks in the database"""
    task_list = []
    tasks_cursor = task_collection.find()
    tasks = await tasks_cursor.to_list(length=None)
    for task in tasks:
        task["_id"] = str(task["_id"])
        task_list.append(task)
    
    return task_list


@app.post("/tasks", 
    status_code=status.HTTP_201_CREATED, 
    response_description="Task added sucessfully"
)
async def create_tasks(task: Task):
    """Creates new task and saves it in the database"""
    date = datetime.now()
    
    task.created_at = date
    task.updated_at = date

    result = await task_collection.insert_one(
        task.model_dump(by_alias=True, exclude=["id"])
    )
    return {
        "message": "Task added successfully"
    }

@app.put("/tasks/{task_id}", status_code=status.HTTP_200_OK, response_model=Task)
async def edit_task(task_id: str, task: TaskEdit):
    """Edits the task"""

    try:
        found = await task_collection.find_one({"_id": ObjectId(task_id)})

    except bson.errors.InvalidId as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"{e}")

    if found is None:
        raise HTTPException(status_code=404, detail="Task with associated id has not been created")
    
    if task.title is None and task.description is None and task.status is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Content to be edited should be supplied")
    

    
    
    edit = await task_collection.update_one({"_id": ObjectId(task_id) }, {"$set": task.model_dump() })
    task_edited = await task_collection.find_one({"_id": ObjectId(task_id) })


    return task_edited


@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK, response_description="Task deleted successully")
async def edit_task(task_id: str):
    """Edits the task"""

    try:
        found = await task_collection.find_one({"_id": ObjectId(task_id)})

    except bson.errors.InvalidId as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"{e}")

    if found is None:
        raise HTTPException(status_code=404, detail="Task with associated id has not been created")
    
    
    edit = await task_collection.delete_one({"_id": ObjectId(task_id) })


    return HTTPException(status_code=200, detail="Task deleted successfully")


@app.get("/")
async def root():
    return {"message": "Hello World"}