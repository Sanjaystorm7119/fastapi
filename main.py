from fastapi import FastAPI , HTTPException
from typing import List
from models import User,Gender,Role
from uuid import uuid4,UUID

app = FastAPI()
db: List[User] = [
    User(id=UUID("00b2957f-4b06-4729-80d1-90944be3406c"),
         firstName="san",
         lastName="jay",
         gender=Gender.male,
         roles=[Role.student],
         midName=None
         ),
    User(id=UUID("8a2b3c2e-50a8-4518-830f-fb627b3bc186"),
         firstName="san",
         lastName="jana",
         gender=Gender. female,
         roles=[Role.admin,Role.user],
         midName=None
         ),
]

@app.get('/')
async def read_root():
    return {"msg" : "hello world"}

@app.get('/api/v1/users')
async def fetch_users():
    return db

@app.post('/api/v1/users')
async def add_user(user:User):
    db.append(user)
    return {"id":user.id}

# @app.delete('/api/v1/users/{user_id}')
# async def delete_user(user_id:UUID):
#     for user in db:
#         if user.id == user_id:
#             db.remove(user)
# ##would still show 200 even if the id is not available
#             return

@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404,detail=f"user with id {user_id} does not exist"
        )







