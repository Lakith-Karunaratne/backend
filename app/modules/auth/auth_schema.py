from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class AddUserSchema(BaseModel):
    id : int
    username : str
    email : EmailStr
    password: str
    
    class Config:
        orm_mode = True

class UpdateUserSchema(BaseModel):
    id : int
    username : str
    new_email : EmailStr
    # password: str
    
    class Config:
        orm_mode = True

class DeleteUserSchema(BaseModel):
    id : int
    username : str | None = None
    # email : EmailStr | None = None
    
    class Config:
        orm_mode = True