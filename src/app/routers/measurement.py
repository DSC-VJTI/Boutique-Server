from typing import List

from database.db import get_db
from database.queries.measurement import Measurement
from database.schemas.measurement import MeasurementBase
from database.schemas.measurement import MeasurementSchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from helpers.measurement import deserialize
from helpers.measurement import serialize
from middleware.auth import is_authenticated
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/admin/measurements", tags=["measurements"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[MeasurementSchema]
)
def get_all_measurements(
    _: int = Depends(is_authenticated), db: Session = Depends(get_db)
):
    m_list = Measurement.get_all_measurements(db)
    return [MeasurementSchema(**deserialize(m)) for m in m_list]


@router.get(
    "/{m_id}", status_code=status.HTTP_200_OK, response_model=MeasurementSchema
)
def get_measurement_by_id(
    m_id: int,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return MeasurementSchema(
        **deserialize(Measurement.get_measurement_by_id(m_id, db))
    )


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=MeasurementSchema
)
def create_measurement(
    m: MeasurementBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    db_m = Measurement.create_measurement(serialize(m), db)
    return MeasurementSchema(**deserialize(db_m))


@router.put(
    "/{m_id}", status_code=status.HTTP_200_OK, response_model=MeasurementSchema
)
def update_measurement(
    m_id: int,
    m: MeasurementBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    db_m = Measurement.update_measurement(m_id, serialize(m), db)
    return MeasurementSchema(**deserialize(db_m))


@router.delete("/{m_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(
    m_id: int,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    Measurement.delete_measurement(m_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
