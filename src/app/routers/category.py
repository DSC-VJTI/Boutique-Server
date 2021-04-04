from typing import List

from database.db import get_db
from database.queries.category import Category
from database.queries.category import SubCategory
from database.schemas.category import CategoryBase
from database.schemas.category import CategorySchema
from database.schemas.category import SubCategoryBase
from database.schemas.category import SubCategorySchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from middleware.auth import is_authenticated
from sqlalchemy.orm import Session

cat_router = APIRouter(prefix="/api/admin/categories", tags=["categories"])
sub_cat_router = APIRouter(
    prefix="/api/admin/sub_categories", tags=["sub-categories"]
)


@cat_router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[CategorySchema]
)
def get_all_categories(db: Session = Depends(get_db)):
    return Category.get_all_categories(db)


@cat_router.get(
    "/{c_id}", status_code=status.HTTP_200_OK, response_model=CategorySchema
)
def get_category_by_id(c_id: int, db: Session = Depends(get_db)):
    return Category.get_category_by_id(c_id, db)


@cat_router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=CategorySchema
)
def create_category(
    c: CategoryBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return Category.create_category(c, db)


@cat_router.put(
    "/{c_id}", status_code=status.HTTP_200_OK, response_model=CategorySchema
)
def update_category(
    c_id: int,
    c: CategoryBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return Category.update_category(c_id, c, db)


@cat_router.delete("/{c_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    c_id: int,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    Category.delete_category(c_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@sub_cat_router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[SubCategorySchema]
)
def get_all_sub_categories(db: Session = Depends(get_db)):
    return SubCategory.get_all_sub_categories(db)


@sub_cat_router.get(
    "/{s_id}", status_code=status.HTTP_200_OK, response_model=SubCategorySchema
)
def get_sub_category_by_id(s_id: int, db: Session = Depends(get_db)):
    return SubCategory.get_sub_category_by_id(s_id, db)


@sub_cat_router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=SubCategorySchema
)
def create_sub_category(
    s: SubCategoryBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return SubCategory.create_sub_category(s, db)


@sub_cat_router.put(
    "/{s_id}", status_code=status.HTTP_200_OK, response_model=SubCategorySchema
)
def update_sub_category(
    s_id: int,
    s: SubCategoryBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return SubCategory.update_sub_category(s_id, s, db)


@sub_cat_router.delete("/{s_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sub_category(
    s_id: int,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    SubCategory.delete_sub_category(s_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
