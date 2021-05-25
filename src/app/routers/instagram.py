from typing import List

from database.db import get_db
from database.queries.instagram import Instagram
from database.schemas.instagram import InstagramBase
from database.schemas.instagram import InstagramSchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from middleware.auth import is_admin
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/admin/instagram", tags=["instagram"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[InstagramSchema],
)
def get_all_instagram_images(db: Session = Depends(get_db)):
    return Instagram.get_all_instagram_images(db)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=InstagramSchema
)
def create_instagram_image(
    image: InstagramBase,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    return Instagram.create_instagram_image(image, db)


@router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_instagram(
    image_id: int,
    _: bool = Depends(is_admin),
    db: Session = Depends(get_db),
):
    Instagram.delete_instagram_image(image_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
