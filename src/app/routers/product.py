from typing import List

from database.db import get_db
from database.queries.product import Product
from database.schemas.product import ProductBase
from database.schemas.product import ProductSchema
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from helpers.product import product_model_to_schema
from middleware.auth import is_authenticated
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/admin/products", tags=["products"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[ProductSchema]
)
def get_all_products(db: Session = Depends(get_db)):
    products = Product.get_all_products(db)
    for i in range(len(products)):
        products[i] = product_model_to_schema(products[i], db)
    return products


@router.get(
    "/{p_id}", status_code=status.HTTP_200_OK, response_model=ProductSchema
)
def get_product_by_id(p_id: int, db: Session = Depends(get_db)):
    return product_model_to_schema(Product.get_product_by_id(p_id, db), db)


@router.get(
    "/category/{c_id}",
    status_code=status.HTTP_200_OK,
    response_model=List[ProductSchema],
)
def get_products_by_category(c_id: int, db: Session = Depends(get_db)):
    products = Product.get_products_by_category(c_id, db)
    for i in range(len(products)):
        products[i] = product_model_to_schema(products[i], db)
    return products


@router.get(
    "/sub_category/{s_id}",
    status_code=status.HTTP_200_OK,
    response_model=List[ProductSchema],
)
def get_products_by_sub_category(s_id: int, db: Session = Depends(get_db)):
    products = Product.get_products_by_sub_category(s_id, db)
    for i in range(len(products)):
        products[i] = product_model_to_schema(products[i], db)
    return products


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=ProductSchema
)
def create_product(
    p: ProductBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return product_model_to_schema(Product.create_product(p, db), db)


@router.put(
    "/{p_id}", status_code=status.HTTP_200_OK, response_model=ProductSchema
)
def update_product(
    p_id: int,
    p: ProductBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    return product_model_to_schema(Product.update_product(p_id, p, db), db)


@router.delete("/{p_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    p_id: int,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    Product.delete_product(p_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
