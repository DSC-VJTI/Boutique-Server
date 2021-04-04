from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

from ..db import Base
from .category import Category
from .category import SubCategory

product_sub_category_table = Table(
    "products_sub_categories",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("sub_category_id", Integer, ForeignKey("sub_categories.id")),
)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    category_id = Column(Integer, ForeignKey("category.id"))

    category = relationship(
        Category, backref=backref("products", lazy="joined")
    )

    sub_categories = relationship(
        SubCategory,
        secondary=product_sub_category_table,
        backref=backref("products", lazy="joined"),
    )
