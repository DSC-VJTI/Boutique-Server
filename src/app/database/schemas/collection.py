from pydantic import BaseModel


class CollectionBase(BaseModel):
    title: str
    description: str
    image: str


class CollectionSchema(CollectionBase):
    id: int

    class Config:
        orm_mode = True
