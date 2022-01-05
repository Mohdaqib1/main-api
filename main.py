from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=[ "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*'],
)

users=[]
class User(BaseModel):
    id:int
    username: str


@app.get("/user", tags=['users'])

async def root()->dict:

    return {"udata" : users}


@app.post("/user", tags=["users"])

def add_user(user:User) -> dict:

    users.append(user.dict())

    return users[-1]

'''
@app.delete("/user/{id}", tags=["users"])
async def delete_user(id: int) -> dict:
    for user in users:
        if int(user["id"]) == id:
            users.remove(user)
            return {
                "udata": f"User with id {id} has been removed."
            }

    return {
        "udata": f"User with id {id} not found."
    }
    '''
todos = []
class Course(BaseModel):
    id: int
    todo: str

@app.get("/todo", tags=['todos'])

async def root()->dict:

    return {"data" : todos}




@app.post("/todo", tags=["todos"])

def add_todo(todo:Course) -> dict:

    todos.append(todo.dict())

    return todos[-1]

'''
@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed."
            }

    return {
        "data": f"Todo with id {id} not found."
    }'''