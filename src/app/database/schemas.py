from datetime import date

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str


# Base class is schema for request body
class AdminBase(BaseModel):
    username: str
    full_name: str
    password: str


# Schema class is schema for response body and db object
class AdminSchema(AdminBase):
    id: int
    blogs: list = []

    # allows conversion between Pydantic and ORMs

    class Config:
        orm_mode = True


class BlogBase(BaseModel):
    title: str
    content: str


class BlogSchema(BlogBase):
    id: int
    created_on: date
    last_updated: date
    author_id: int

    class Config:
        orm_mode = True
