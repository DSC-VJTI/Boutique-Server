from pydantic import BaseModel


# Base class is schema for request body
class AdminBase(BaseModel):
    username: str
    full_name: str
    password: str
    is_admin: bool


# Schema class is schema for response body and db object
class AdminSchema(AdminBase):
    id: int
    blogs: list = []

    # allows conversion between Pydantic and ORMs

    class Config:
        orm_mode = True
