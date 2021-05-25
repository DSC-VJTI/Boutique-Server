from exceptions.collection import collection_already_exists_exception
from exceptions.collection import collection_not_found_exception
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..models import collection
from ..schemas.collection import CollectionBase


class Collection:
    @staticmethod
    def get_all_collections(db: Session):
        return db.query(collection.Collection).all()

    @staticmethod
    def get_collection_by_id(c_id: int, db: Session):
        db_c = (
            db.query(collection.Collection)
            .filter(collection.Collection.id == c_id)
            .first()
        )
        if not db_c:
            raise collection_not_found_exception
        return db_c

    @staticmethod
    def create_collection(c: CollectionBase, db: Session):
        try:
            db_c = collection.Collection(**c.dict())
            db.add(db_c)
            db.commit()
            db.refresh(db_c)
            return db_c
        except IntegrityError:
            raise collection_already_exists_exception

    @staticmethod
    def update_collection(c_id: int, c: CollectionBase, db: Session):
        _ = Collection.get_collection_by_id(c_id, db)
        db.query(collection.Collection).filter(
            collection.Collection.id == c_id
        ).update(c, synchronize_session="fetch")
        db.commit()
        return Collection.get_collection_by_id(c_id, db)

    @staticmethod
    def delete_collection(c_id: int, db: Session):
        _ = Collection.get_collection_by_id(c_id, db)
        db.query(collection.Collection).filter(
            collection.Collection.id == c_id
        ).delete(synchronize_session="fetch")
        db.commit()
        return
