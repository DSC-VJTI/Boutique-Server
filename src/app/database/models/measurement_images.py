from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from ..db import Base


class MeasurementImage(Base):
    __tablename__ = "measurement_images"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    measurement_id = Column(Integer, ForeignKey("measurements.id"))
