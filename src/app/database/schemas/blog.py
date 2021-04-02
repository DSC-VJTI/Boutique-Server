from datetime import date

from pydantic import BaseModel


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
