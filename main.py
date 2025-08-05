from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, user_update_request
from uuid import UUID

app = FastAPI()

db: List[User] = [
    User(id=UUID("00b2957f-4b06-4729-80d1-90944be3406c"),
         firstName="san",
         lastName="jay",
         gender=Gender.male,
         roles=[Role.student],
         midName=None),
    User(id=UUID("8a2b3c2e-50a8-4518-830f-fb627b3bc186"),
         firstName="san",
         lastName="jana",
         gender=Gender.female,
         roles=[Role.admin, Role.user],
         midName=None),
]

@app.get('/')
async def read_root():
    return {"msg": "hello world"}

@app.get('/api/v1/users')
async def fetch_users():
    return db

@app.post('/api/v1/users')
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"msg": f"user {user_id} deleted"}
    raise HTTPException(
        status_code=404, detail=f"user with id {user_id} does not exist"
    )

@app.put('/api/v1/users/{user_id}')
async def update_user(user_update: user_update_request, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.firstName is not None:
                user.firstName = user_update.firstName
            if user_update.lastName is not None:
                user.lastName = user_update.lastName
            if user_update.midName is not None:
                user.midName = user_update.midName
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"msg": f"User {user_id} updated"}
    
    raise HTTPException(
        status_code=404, detail=f"User with id {user_id} does not exist"
    )
