from typing import List

from database.db import get_db
from database.queries.category import SubCategory
from database.schemas.category import SubCategoryBase
from database.schemas.category import SubCategorySchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from middleware.auth import is_admin
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/admin/sub_categories", tags=["sub-categories"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[SubCategorySchema]
)
def get_all_sub_categories(db: Session = Depends(get_db)):
    return SubCategory.get_all_sub_categories(db)


@router.get(
    "/{s_id}", status_code=status.HTTP_200_OK, response_model=SubCategorySchema
)
def get_sub_category_by_id(s_id: int, db: Session = Depends(get_db)):
    return SubCategory.get_sub_category_by_id(s_id, db)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=SubCategorySchema
)
def create_sub_category(
    s: SubCategoryBase,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    return SubCategory.create_sub_category(s, db)


@router.put(
    "/{s_id}", status_code=status.HTTP_200_OK, response_model=SubCategorySchema
)
def update_sub_category(
    s_id: int,
    s: SubCategoryBase,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    return SubCategory.update_sub_category(s_id, s, db)


@router.delete("/{s_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sub_category(
    s_id: int,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    SubCategory.delete_sub_category(s_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
