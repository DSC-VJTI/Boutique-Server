from typing import List

from database.db import get_db
from database.queries.material import Material
from database.schemas.material import MaterialBase
from database.schemas.material import MaterialSchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from middleware.auth import is_authenticated
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/admin/materials", tags=["materials"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[MaterialSchema]
)
def get_all_materials(
    _: int = Depends(is_authenticated), db: Session = Depends(get_db)
):
    return Material.get_all_materials(db)


@router.get(
    "/{m_id}", status_code=status.HTTP_200_OK, response_model=MaterialSchema
)
def get_material_by_id(
    m_id: int,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return Material.get_material_by_id(m_id, db)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=MaterialSchema
)
def create_material(
    m: MaterialBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return Material.create_material(m, db)


@router.put(
    "/{m_id}", status_code=status.HTTP_200_OK, response_model=MaterialSchema
)
def update_material(
    m_id: int,
    m: MaterialBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return Material.update_material(m_id, m, db)


@router.delete("/{m_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_material(
    m_id: int,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    Material.delete_material(m_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
