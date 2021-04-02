from datetime import date
from typing import Dict

from pydantic import BaseModel


class MeasurementBase(BaseModel):
    client_name: str
    dl: str
    l: Dict[str, str]
    ac: str
    c: str
    bc: str
    w: str
    lw: str
    h: str
    sh: str
    sl: Dict[str, str]
    n: Dict[str, str]
    arm: str

    bottom_w: Dict[str, str]
    bottom_l: str
    bottom_th: str
    bottom_c: str
    bottom_k: str
    bottom_r: str


class MeasurementSchema(MeasurementBase):
    id: int
    created_on: date
    last_updated: date

    class Config:
        orm_mode = True
