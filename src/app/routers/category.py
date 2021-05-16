from typing import List

from database.db import get_db
from database.queries.category import Category
from database.schemas.category import CategoryBase
from database.schemas.category import CategorySchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from middleware.auth import is_admin
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/admin/categories", tags=["categories"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[CategorySchema]
)
def get_all_categories(db: Session = Depends(get_db)):
    return Category.get_all_categories(db)


@router.get(
    "/{c_id}", status_code=status.HTTP_200_OK, response_model=CategorySchema
)
def get_category_by_id(c_id: int, db: Session = Depends(get_db)):
    return Category.get_category_by_id(c_id, db)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=CategorySchema
)
def create_category(
    c: CategoryBase,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    return Category.create_category(c, db)


@router.put(
    "/{c_id}", status_code=status.HTTP_200_OK, response_model=CategorySchema
)
def update_category(
    c_id: int,
    c: CategoryBase,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    return Category.update_category(c_id, c, db)


@router.delete("/{c_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    c_id: int,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    Category.delete_category(c_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
