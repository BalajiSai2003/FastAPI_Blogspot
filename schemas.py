
######################## SCHEMAS FOR PYDANTIC MODELS ######################

from pydantic import BaseModel , EmailStr

from datetime import datetime

from typing import List, Optional



class LoginSchema(BaseModel):
    email : EmailStr
    password : str



class Token(BaseModel):
    access_token : str
    token_type  : str


class Token_data(BaseModel):
    id : Optional[str] = None








class UserCreate(BaseModel):
    name : str
    email : EmailStr
    password : str

class UserResponce(BaseModel):
    name : str
    email : EmailStr
    id : int
    created_at : datetime

    class Config:
        orm_mode = True


class UpadteUserName(BaseModel):
    name : str

    class Config:
        orm_mode = True

class UpadteUserEmail(BaseModel):
    email : EmailStr

    class Config:
        orm_mode = True

class UpdateUserPassword(BaseModel):
    password : str

    class Config:
        orm_mode = True








class BasePost(BaseModel):
    title: str
    content: str
    published: bool =True


class CreatePost(BasePost):
    pass

class UpdatePost(BasePost):
    pass

class Post(BaseModel):
    author_id: int
    id : int
    created_at: datetime
    author : UserResponce
    comments: List["Comment"] = []


    class Config:
        orm_mode = True







class CommentBase(BaseModel):
    content: str
    post_id: int


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    author: UserResponce
    post: Post

    class Config:
        orm_mode = True