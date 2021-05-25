from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from ..db import Base


class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    description = Column(String)
    image = Column(String)
