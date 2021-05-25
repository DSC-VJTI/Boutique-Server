from exceptions.instagram import image_not_found_exception
from sqlalchemy.orm import Session

from ..models import instagram
from ..schemas.instagram import InstagramBase


class Instagram:
    @staticmethod
    def get_all_instagram_images(db: Session):
        return db.query(instagram.Instagram).all()

    @staticmethod
    def get_instagram_image_by_id(image_id: int, db: Session):
        db_image = (
            db.query(instagram.Instagram)
            .filter(instagram.Instagram.id == image_id)
            .first()
        )
        if not db_image:
            raise image_not_found_exception
        return db_image

    @staticmethod
    def create_instagram_image(image: InstagramBase, db: Session):
        db_image = instagram.Instagram(**image.dict())
        db.add(db_image)
        db.commit()
        db.refresh(db_image)
        return db_image

    @staticmethod
    def delete_instagram_image(image_id: int, db: Session):
        _ = Instagram.get_instagram_image_by_id(image_id, db)
        db.query(instagram.Instagram).filter(
            instagram.Instagram.id == image_id
        ).delete(synchronize_session="fetch")
        db.commit()
        return
