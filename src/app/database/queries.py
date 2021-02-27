from datetime import date

from exceptions.admin import admin_already_exists_exception
from exceptions.blog import blog_already_exists_exception
from exceptions.blog import blog_not_found_exception
from helpers.auth import get_password_hash
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from . import models
from . import schemas


class Admin:
    @staticmethod
    def get_admin_by_id(id: int, db: Session):
        return db.query(models.Admin).filter(models.Admin.id == id).first()

    @staticmethod
    def get_admin_by_username(username: str, db: Session):
        return (
            db.query(models.Admin)
            .filter(models.Admin.username == username)
            .first()
        )

    @staticmethod
    def create_admin(admin: schemas.AdminBase, db: Session):
        try:
            admin.password = get_password_hash(admin.password)
            db_user = models.Admin(**admin.dict())
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError:
            raise admin_already_exists_exception


class Blog:
    @staticmethod
    def get_all_blogs(db: Session):
        return db.query(models.Blog).all()

    @staticmethod
    def get_all_blogs_of_author(author_id: int, db: Session):
        return (
            db.query(models.Blog)
            .filter(models.Blog.author_id == author_id)
            .all()
        )

    @staticmethod
    def create_blog(author_id: int, blog: schemas.BlogBase, db: Session):
        try:
            today = date.today()
            db_blog = models.Blog(
                **blog.dict(),
                author_id=author_id,
                created_on=today,
                last_updated=today
            )
            db.add(db_blog)
            db.commit()
            db.refresh(db_blog)
            return db_blog
        except IntegrityError:
            raise blog_already_exists_exception

    @staticmethod
    def view_blog(blog_id: int, db: Session):
        db_blog = (
            db.query(models.Blog).filter(models.Blog.id == blog_id).first()
        )
        if not db_blog:
            raise blog_not_found_exception
        return db_blog

    @staticmethod
    def update_blog(blog_id: int, blog: schemas.BlogBase, db: Session):
        db_blog = (
            db.query(models.Blog).filter(models.Blog.id == blog_id).first()
        )
        if not db_blog:
            raise blog_not_found_exception
        db_blog.title = blog.title
        db_blog.content = blog.content
        db_blog.last_updated = date.today()
        db.commit()
        db.refresh(db_blog)
        return db_blog

    @staticmethod
    def delete_blog(blog_id: int, db: Session):
        db_blog = (
            db.query(models.Blog).filter(models.Blog.id == blog_id).first()
        )
        if not db_blog:
            raise blog_not_found_exception
        db.delete(db_blog)
        db.commit()
        return
