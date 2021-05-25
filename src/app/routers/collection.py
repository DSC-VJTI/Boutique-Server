from typing import List

from database.db import get_db
from database.queries.collection import Collection
from database.schemas.collection import CollectionBase
from database.schemas.collection import CollectionSchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from middleware.auth import is_admin
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/admin/collections", tags=["collection"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[CollectionSchema],
)
def get_all_collections(db: Session = Depends(get_db)):
    return Collection.get_all_collections(db)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=CollectionSchema
)
def create_collection(
    c: CollectionBase,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    return Collection.create_collection(c, db)


@router.put(
    "/{c_id}",
    status_code=status.HTTP_200_OK,
    response_model=CollectionSchema,
)
def update_collection(
    c_id: int,
    c: CollectionBase,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    return Collection.update_collection(c_id, c, db)


@router.delete("/{c_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_collection(
    c_id: int,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    Collection.delete_collection(c_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
