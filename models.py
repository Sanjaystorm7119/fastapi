from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    firstName: str
    lastName: str
    midName: Optional[str] = None
    gender: Gender
    roles: List[Role]

class user_update_request(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    midName: Optional[str]
    roles: Optional[List[Role]]
