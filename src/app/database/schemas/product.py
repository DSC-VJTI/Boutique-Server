from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: str
    category_name: int
    sub_categories: List[str]


class ProductSchema(ProductBase):
    id: int

    class Config:
        orm_mode = True
