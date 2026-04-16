from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

# User Model
class User:
    id: int
    name: str
    email: str

# Dummy database
users_db = []

@router.get("/users", response_model=List[User])
def get_users():
    return users_db

@router.post("/users", response_model=User)
def create_user(user: User):
    users_db.append(user)
    return user

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    for idx, db_user in enumerate(users_db):
        if db_user.id == user_id:
            users_db[idx] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    for idx, db_user in enumerate(users_db):
        if db_user.id == user_id:
            del users_db[idx]
            return
    raise HTTPException(status_code=404, detail="User not found")