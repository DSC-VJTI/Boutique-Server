from datetime import date
from typing import Dict

from exceptions.measurement import measurement_not_found_exception
from sqlalchemy.orm import Session

from ..models import measurement as m_model


class Measurement:
    @staticmethod
    def get_all_measurements(db: Session):
        return db.query(m_model.Measurement).all()

    @staticmethod
    def get_measurements_by_client_name(client_name: str, db: Session):
        return (
            db.query(m_model.Measurement)
            .filter(m_model.Measurement.client_name == client_name)
            .all()
        )

    @staticmethod
    def get_measurement_by_id(m_id: int, db: Session):
        db_m = (
            db.query(m_model.Measurement)
            .filter(m_model.Measurement.id == m_id)
            .first()
        )
        if not db_m:
            raise measurement_not_found_exception
        return db_m

    @staticmethod
    def create_measurement(m: Dict[str, str], db: Session):
        today = date.today()
        db_m = m_model.Measurement(**m, created_on=today, last_updated=today)
        db.add(db_m)
        db.commit()
        db.refresh(db_m)
        return db_m

    @staticmethod
    def update_measurement(m_id: int, m: Dict[str, str], db: Session):
        _ = Measurement.get_measurement_by_id(m_id, db)
        m["last_updated"] = date.today()
        db.query(m_model.Measurement).filter(
            m_model.Measurement.id == m_id
        ).update(m, synchronize_session="fetch")
        db.commit()
        return Measurement.get_measurement_by_id(m_id, db)

    @staticmethod
    def delete_measurement(m_id: int, db: Session):
        _ = Measurement.get_measurement_by_id(m_id, db)
        db.query(m_model.Measurement).filter(
            m_model.Measurement.id == m_id
        ).delete(synchronize_session="fetch")
        db.commit()
        return
