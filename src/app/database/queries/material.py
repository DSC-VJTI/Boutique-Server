from datetime import date

from exceptions.material import material_not_found_exception
from sqlalchemy.orm import Session

from ..models import material as m_model
from ..schemas.material import MaterialBase


class Material:
    @staticmethod
    def get_all_materials(db: Session):
        return db.query(m_model.Material).all()

    @staticmethod
    def get_materials_by_client_name(client_name: str, db: Session):
        return (
            db.query(m_model.Material)
            .filter(m_model.Material.client_name == client_name)
            .all()
        )

    @staticmethod
    def get_material_by_id(m_id: int, db: Session):
        db_m = (
            db.query(m_model.Material)
            .filter(m_model.Material.id == m_id)
            .first()
        )
        if not db_m:
            raise material_not_found_exception
        return db_m

    @staticmethod
    def create_material(m: MaterialBase, db: Session):
        today = date.today()
        db_m = m_model.Material(
            **m.dict(), created_on=today, last_updated=today
        )
        db.add(db_m)
        db.commit()
        db.refresh(db_m)
        return db_m

    @staticmethod
    def update_material(m_id: int, m: MaterialBase, db: Session):
        _ = Material.get_material_by_id(m_id, db)
        m_dict = m.dict()
        m_dict["last_updated"] = date.today()
        db.query(m_model.Material).filter(m_model.Material.id == m_id).update(
            m_dict, synchronize_session="fetch"
        )
        db.commit()
        return Material.get_material_by_id(m_id, db)

    @staticmethod
    def delete_material(m_id: int, db: Session):
        _ = Material.get_material_by_id(m_id, db)
        db.query(m_model.Material).filter(m_model.Material.id == m_id).delete(
            synchronize_session="fetch"
        )
        db.commit()
        return
