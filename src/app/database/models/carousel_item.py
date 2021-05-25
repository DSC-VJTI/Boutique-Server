from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from ..db import Base


class CarouselItem(Base):
    __tablename__ = "carousel_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    tag = Column(String)
    description = Column(String)
    image = Column(String)
