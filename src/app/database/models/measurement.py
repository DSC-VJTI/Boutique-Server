from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import String

from ..db import Base


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String)
    created_on = Column(Date)
    last_updated = Column(Date)

    dl = Column(String)
    l = Column(String)  # dict string
    ac = Column(String)
    c = Column(String)
    bc = Column(String)
    w = Column(String)
    lw = Column(String)
    h = Column(String)
    sh = Column(String)
    sl = Column(String)  # dict string
    n = Column(String)  # dict string
    arm = Column(String)

    bottom_w = Column(String)  # dict string
    bottom_l = Column(String)
    bottom_th = Column(String)
    bottom_k = Column(String)
    bottom_c = Column(String)
    bottom_r = Column(String)
