from exceptions.carousel_item import carousel_item_already_exists_exception
from exceptions.carousel_item import carousel_item_not_found_exception
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..models import carousel_item
from ..schemas.carousel_item import CarouselItemBase


class CarouselItem:
    @staticmethod
    def get_all_carousel_items(db: Session):
        return db.query(carousel_item.CarouselItem).all()

    @staticmethod
    def get_carousel_item_by_id(c_item_id: int, db: Session):
        db_c_item = (
            db.query(carousel_item.CarouselItem)
            .filter(carousel_item.CarouselItem.id == c_item_id)
            .first()
        )
        if not db_c_item:
            raise carousel_item_not_found_exception
        return db_c_item

    @staticmethod
    def create_carousel_item(c_item: CarouselItemBase, db: Session):
        try:
            db_c_item = carousel_item.CarouselItem(**c_item.dict())
            db.add(db_c_item)
            db.commit()
            db.refresh(db_c_item)
            return db_c_item
        except IntegrityError:
            raise carousel_item_already_exists_exception

    @staticmethod
    def update_carousel_item(
        c_item_id: int, c_item: CarouselItemBase, db: Session
    ):
        _ = CarouselItem.get_carousel_item_by_id(c_item_id, db)
        db.query(carousel_item.CarouselItem).filter(
            carousel_item.CarouselItem.id == c_item_id
        ).update(c_item, synchronize_session="fetch")
        db.commit()
        return CarouselItem.get_carousel_item_by_id(c_item_id, db)

    @staticmethod
    def delete_carousel_item(c_item_id: int, db: Session):
        _ = CarouselItem.get_carousel_item_by_id(c_item_id, db)
        db.query(carousel_item.CarouselItem).filter(
            carousel_item.CarouselItem.id == c_item_id
        ).delete(synchronize_session="fetch")
        db.commit()
        return
