import os
from datetime import timedelta

from database.db import get_db
from database.queries import Admin
from database.schemas import AdminBase
from database.schemas import AdminSchema
from database.schemas import Token
from exceptions.admin import admin_not_found_exception
from exceptions.admin import incorrect_password_exception
from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import status
from helpers.auth import create_access_token
from helpers.auth import verify_password
from middleware.auth import is_authenticated
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.post("/login", status_code=status.HTTP_200_OK, response_model=Token)
def login(
    username: str = Body(...),
    password: str = Body(...),
    db: Session = Depends(get_db),
):
    admin = Admin.get_admin_by_username(username, db)
    if not admin:
        raise admin_not_found_exception
    if not verify_password(password, admin.password):
        raise incorrect_password_exception
    access_token_expires = timedelta(
        minutes=int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )
    access_token = create_access_token(
        data={"id": admin.id, "username": admin.username},
        expires_delta=access_token_expires,
    )
    return Token(access_token=str(access_token))


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=Token
)
def register(
    body: AdminBase,
    _: int = Depends(is_authenticated),
    db: Session = Depends(get_db),
):
    admin = Admin.create_admin(body, db)
    access_token_expires = timedelta(
        minutes=int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )
    access_token = create_access_token(
        data={"id": admin.id, "username": admin.username},
        expires_delta=access_token_expires,
    )
    return Token(access_token=str(access_token))


@router.get("/", status_code=status.HTTP_200_OK, response_model=AdminSchema)
def get_admin(
    admin_id: int = Depends(is_authenticated), db: Session = Depends(get_db)
):
    admin = Admin.get_admin_by_id(admin_id, db)
    if not admin:
        raise admin_not_found_exception
    return admin
