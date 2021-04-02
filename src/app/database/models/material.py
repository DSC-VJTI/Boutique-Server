from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from ..db import Base


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String)

    top = Column(String)
    bottom = Column(String)
    dupatta = Column(String)
    lining = Column(String)

    laces = Column(String)
    emroidery = Column(String)
    piping = Column(String)
    zip = Column(String)
    buttons = Column(String)

    tailoring = Column(String)
    convayance = Column(String)
    overheads = Column(String)
