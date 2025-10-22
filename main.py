from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

users = []

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/users/", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/", response_model=List[User])
def read_users():
    return users

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for user in users:
        if user.id == user_id:
            user.name = updated_user.name
            user.age = updated_user.age
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    original_length = len(users)
    users = [user for user in users if user.id != user_id]
    if len(users) == original_length:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}