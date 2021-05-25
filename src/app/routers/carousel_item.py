from typing import List

from database.db import get_db
from database.queries.carousel_item import CarouselItem
from database.schemas.carousel_item import CarouselItemBase
from database.schemas.carousel_item import CarouselItemSchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from middleware.auth import is_admin
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/admin/carousel", tags=["carousel"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[CarouselItemSchema],
)
def get_all_carousel_items(db: Session = Depends(get_db)):
    return CarouselItem.get_all_carousel_items(db)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=CarouselItemSchema
)
def create_carousel_item(
    c_item: CarouselItemBase,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    return CarouselItem.create_carousel_item(c_item, db)


@router.put(
    "/{c_item_id}",
    status_code=status.HTTP_200_OK,
    response_model=CarouselItemSchema,
)
def update_carousel_item(
    c_item_id: int,
    c_item: CarouselItemBase,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    return CarouselItem.update_carousel_item(c_item_id, c_item, db)


@router.delete("/{c_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carousel_item(
    c_item_id: int,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    CarouselItem.delete_carousel_item(c_item_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
