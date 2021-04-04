from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category_name: str
    sub_categories: List


class ProductSchema(ProductBase):
    id: int

    class Config:
        orm_mode = True
