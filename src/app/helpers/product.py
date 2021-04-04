from database.models.product import Product
from database.queries.category import Category
from database.schemas.product import ProductSchema
from sqlalchemy.orm import Session


def product_model_to_schema(product: Product, db: Session):
    p_dict = product.__dict__
    p_dict["category_name"] = Category.get_category_by_id(
        product.category_id, db
    ).name
    p_dict.pop("category_id")
    p_dict["sub_categories"] = [s.name for s in product.sub_categories]
    return ProductSchema(**p_dict)
