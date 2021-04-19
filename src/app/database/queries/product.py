from exceptions.product import product_already_exists_exception
from exceptions.product import product_not_found_exception
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..models import product as product_model
from ..models.product_images import ProductImage
from ..schemas.product import ProductBase
from .category import Category
from .category import SubCategory


class Product:
    @staticmethod
    def get_all_products(db: Session):
        return db.query(product_model.Product).all()

    @staticmethod
    def get_product_by_id(p_id: int, db: Session):
        db_product = db.query(product_model.Product).filter_by(id=p_id).first()
        if not db_product:
            raise product_not_found_exception
        return db_product

    @staticmethod
    def get_products_by_category(c_id: int, db: Session):
        return (
            db.query(product_model.Product).filter_by(category_id=c_id).all()
        )

    @staticmethod
    def get_products_by_sub_category(s_id: int, db: Session):
        return SubCategory.get_sub_category_by_id(s_id, db).products

    @staticmethod
    def create_product(p: ProductBase, db: Session):
        db_category = Category.get_category_by_name(p.category_name, db)
        db_product = product_model.Product(
            name=p.name,
            description=p.description,
            info=p.info,
            price=p.price,
            discount_price=p.discount_price,
            category_id=db_category.id,
        )
        db.add(db_product)
        for s in p.sub_categories:
            db_sub_category = SubCategory.get_sub_category_by_name(s, db)
            db_sub_category.products.append(db_product)
            db.add(db_sub_category)
        for product_image in p.images:
            new_image = ProductImage(image_url=product_image)
            db_product.images.append(new_image)
            db.add(new_image)

        try:
            db.commit()
            return db_product
        except IntegrityError:
            raise product_already_exists_exception

    @staticmethod
    def update_product(p_id: int, p: ProductBase, db: Session):
        db_product = Product.get_product_by_id(p_id, db)
        db_category = Category.get_category_by_name(p.category_name, db)
        db_product.sub_categories.clear()
        db_product.images.clear()

        db_product.name = p.name
        db_product.description = p.description
        db_product.info = p.info
        db_product.price = p.price
        db_product.discount_price = p.discount_price
        db_product.category_id = db_category.id

        db.add(db_product)

        for s in p.sub_categories:
            db_sub_category = SubCategory.get_sub_category_by_name(s, db)
            db_sub_category.products.append(db_product)
            db.add(db_sub_category)

        for image_url in p.images:
            new_image = ProductImage(image_url=image_url)
            db_product.images.append(new_image)
            db.add(new_image)

        try:
            db.commit()
            db.refresh(db_product)
            return db_product
        except IntegrityError:
            raise product_already_exists_exception

    @staticmethod
    def delete_product(p_id: int, db: Session):
        db_product = Product.get_product_by_id(p_id, db)
        for s in db_product.sub_categories:
            s.products.remove(db_product)
            db.add(s)
        db.delete(db_product)
        db.commit()
        return
