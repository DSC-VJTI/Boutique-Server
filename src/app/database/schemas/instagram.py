from pydantic import BaseModel


class InstagramBase(BaseModel):
    image: str


class InstagramSchema(InstagramBase):
    id: int

    class Config:
        orm_mode = True
