from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from ..db import Base


class Instagram(Base):
    __tablename__ = "instagram_images"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
