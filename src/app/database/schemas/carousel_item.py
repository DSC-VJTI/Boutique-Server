from pydantic import BaseModel


class CarouselItemBase(BaseModel):
    title: str
    tag: str
    description: str
    image: str


class CarouselItemSchema(CarouselItemBase):
    id: int

    class Config:
        orm_mode = True
