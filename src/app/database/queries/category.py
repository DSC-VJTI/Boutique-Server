from exceptions.category import category_already_exists_exception
from exceptions.category import category_not_found_exception
from exceptions.category import sub_category_already_exists_exception
from exceptions.category import sub_category_not_found_exception
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..models import category as category_model
from ..schemas.category import CategoryBase
from ..schemas.category import SubCategoryBase


class Category:
    @staticmethod
    def get_all_categories(db: Session):
        return db.query(category_model.Category).all()

    @staticmethod
    def get_category_by_id(c_id: int, db: Session):
        db_category = (
            db.query(category_model.Category).filter_by(id=c_id).first()
        )
        if not db_category:
            raise category_not_found_exception
        return db_category

    @staticmethod
    def get_category_by_name(c_name: int, db: Session):
        db_category = (
            db.query(category_model.Category).filter_by(name=c_name).first()
        )
        if not db_category:
            raise category_not_found_exception
        return db_category

    @staticmethod
    def create_category(c: CategoryBase, db: Session):
        try:
            db_category = category_model.Category(**c.dict())
            db.add(db_category)
            db.commit()
            db.refresh(db_category)
            return db_category
        except IntegrityError:
            raise category_already_exists_exception

    @staticmethod
    def update_category(c_id: int, c: CategoryBase, db: Session):
        _ = Category.get_category_by_id(c_id, db)
        db.query(category_model.Category).filter_by(id=c_id).update(
            c, synchronize_session="fetch"
        )
        db.commit()
        return Category.get_category_by_id(c_id, db)

    @staticmethod
    def delete_category(c_id: int, db: Session):
        db_category = Category.get_category_by_id(c_id, db)
        for s in db_category.sub_categories:
            SubCategory.delete_sub_category(s.id, db)
        for p in db_category.products:
            db.delete(p)
        db.delete(db_category)
        db.commit()
        return


class SubCategory:
    @staticmethod
    def get_all_sub_categories(db: Session):
        return db.query(category_model.SubCategory).all()

    @staticmethod
    def get_sub_category_by_id(s_id: int, db: Session):
        db_sub_category = (
            db.query(category_model.SubCategory).filter_by(id=s_id).first()
        )
        if not db_sub_category:
            raise sub_category_not_found_exception
        return db_sub_category

    @staticmethod
    def get_sub_category_by_name(s_name: int, db: Session):
        db_sub_category = (
            db.query(category_model.SubCategory).filter_by(name=s_name).first()
        )
        if not db_sub_category:
            raise sub_category_not_found_exception
        return db_sub_category

    @staticmethod
    def create_sub_category(s: SubCategoryBase, db: Session):
        try:
            db_category = Category.get_category_by_name(s.category_name, db)
            db_sub_category = category_model.SubCategory(
                name=s.name, category_id=db_category.id
            )
            db.add(db_sub_category)
            db.commit()
            db.refresh(db_sub_category)
            return db_sub_category
        except IntegrityError:
            raise sub_category_already_exists_exception

    @staticmethod
    def update_sub_category(s_id: int, s: SubCategoryBase, db: Session):
        db_sub_category = SubCategory.get_sub_category_by_id(s_id, db)
        db_sub_category.name = s.name
        db_category = Category.get_category_by_name(s.category_name, db)
        db_sub_category.category_id = db_category.id
        db.add(db_sub_category)
        db.commit()
        db.refresh(db_sub_category)
        return db_sub_category

    @staticmethod
    def delete_sub_category(s_id: int, db: Session):
        db_sub_category = SubCategory.get_sub_category_by_id(s_id, db)
        for p in db_sub_category.products:
            p.sub_categories.remove(db_sub_category)
            db.add(p)
        db.delete(db_sub_category)
        db.commit()
        return
