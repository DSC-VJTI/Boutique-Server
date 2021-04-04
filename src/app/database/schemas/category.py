from typing import List

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategorySchema(CategoryBase):
    id: int
    sub_categories: List = []
    products: List = []

    class Config:
        orm_mode = True


class SubCategoryBase(BaseModel):
    name: str
    category_name: str


class SubCategorySchema(BaseModel):
    id: int
    name: str
    category_id: int
    products: List = []

    class Config:
        orm_mode = True
