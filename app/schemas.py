from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional


# -------------------- Schema --------------------
#it is like the layer between the req, response and the API, only required information if we need to pass or want we use it make class
#the magic is possible due to pydantic

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id:int
    email:EmailStr
    class Config:
        from_attributes = True 

class Post(PostBase):
    id:int
    created_at: datetime
    owner_id:int
    owner:UserOut
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[int] = None