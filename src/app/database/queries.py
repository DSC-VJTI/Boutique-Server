from exceptions.admin import admin_already_exists_exception
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
