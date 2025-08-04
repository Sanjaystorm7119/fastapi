from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional ,List
from enum import Enum


class Gender(str,Enum):
    male="male"
    female="female"

class Role(str,Enum):
    admin="admin"
    user="user"
    student="student"

class User(BaseModel):
    id : Optional[UUID]=uuid4()
    firstName : str
    lastName : str
    midName : Optional[str]
    gender : Gender
    roles : List[Role]