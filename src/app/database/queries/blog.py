from datetime import date

from exceptions.blog import blog_already_exists_exception
from exceptions.blog import blog_not_found_exception
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..models import blog as blog_model
from ..schemas.blog import BlogBase


class Blog:
    @staticmethod
    def get_all_blogs(db: Session):
        return db.query(blog_model.Blog).all()

    @staticmethod
    def get_all_blogs_of_author(author_id: int, db: Session):
        return (
            db.query(blog_model.Blog)
            .filter(blog_model.Blog.author_id == author_id)
            .all()
        )

    @staticmethod
    def create_blog(author_id: int, blog: BlogBase, db: Session):
        try:
            today = date.today()
            db_blog = blog_model.Blog(
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
            db.query(blog_model.Blog)
            .filter(blog_model.Blog.id == blog_id)
            .first()
        )
        if not db_blog:
            raise blog_not_found_exception
        return db_blog

    @staticmethod
    def update_blog(blog_id: int, blog: BlogBase, db: Session):
        db_blog = (
            db.query(blog_model.Blog)
            .filter(blog_model.Blog.id == blog_id)
            .first()
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
            db.query(blog_model.Blog)
            .filter(blog_model.Blog.id == blog_id)
            .first()
        )
        if not db_blog:
            raise blog_not_found_exception
        db.delete(db_blog)
        db.commit()
        return
