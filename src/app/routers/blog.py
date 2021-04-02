from typing import List

from database.db import get_db
from database.queries.blog import Blog
from database.schemas.blog import BlogBase
from database.schemas.blog import BlogSchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from middleware.auth import is_authenticated
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/blogs", tags=["blogs"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[BlogSchema]
)
def get_all_blogs(db: Session = Depends(get_db)):
    return Blog.get_all_blogs(db)


@router.get(
    "/{blog_id}", status_code=status.HTTP_200_OK, response_model=BlogSchema
)
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    return Blog.view_blog(blog_id, db)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=BlogSchema
)
def create_blog(
    blog: BlogBase,
    admin_id: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return Blog.create_blog(admin_id, blog, db)


@router.put(
    "/{blog_id}", status_code=status.HTTP_200_OK, response_model=BlogSchema
)
def update_blog(
    blog_id: int,
    blog: BlogBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return Blog.update_blog(blog_id, blog, db)


@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(
    blog_id: int,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    Blog.delete_blog(blog_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
