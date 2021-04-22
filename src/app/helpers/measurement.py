import json
from typing import Dict

from database.models.measurement import Measurement
from database.schemas.measurement import MeasurementBase

keys = ["l", "sl", "n", "bottom_w"]


def serialize(m: MeasurementBase) -> Dict[str, str]:
    m_dict = m.dict()
    for key in keys:
        m_dict[key] = json.dumps(m_dict[key])
    return m_dict


def deserialize(m: Measurement) -> Dict[str, Dict[str, str]]:
    m_dict = m.__dict__
    for key in keys:
        m_dict[key] = json.loads(m_dict[key])
    m_dict["images"]=[x.image_url for x in m.images]
    return m_dict
