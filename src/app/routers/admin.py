from fastapi import APIRouter, status, Body, Depends
from sqlalchemy.orm import Session
from datetime import timedelta
import os

from helpers.auth import create_access_token, verify_password
from database.schemas import AdminBase, AdminSchema, Token
from database.queries import Admin
from database.db import get_db
from middleware.auth import is_autheticated

from exceptions.admin import admin_not_found_exception, incorrect_password_exception, admin_already_exists_exception

router = APIRouter(
    prefix="/api/admin",
    tags=["admin"]
)

@router.post("/login", status_code=status.HTTP_200_OK, response_model=Token)
def login(username: str = Body(...), password: str = Body(...), db: Session = Depends(get_db)):
    admin = Admin.get_admin_by_username(username, db)
    if not admin:
        raise admin_not_found_exception
    if not verify_password(password, admin.password):
        raise incorrect_password_exception
    access_token_expires = timedelta(minutes=int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={
            "id": admin.id,
            "username" : admin.username
        },
        expires_delta=access_token_expires
    )
    return Token(access_token=str(access_token))

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=Token)
def register(body: AdminBase, _ : int = Depends(is_autheticated), db: Session = Depends(get_db)):
    admin = Admin.create_admin(body, db)
    access_token_expires = timedelta(minutes=int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={
            "id": admin.id,
            "username" : admin.username
        },
        expires_delta=access_token_expires
    )
    return Token(access_token=str(access_token))

@router.get("/", status_code=status.HTTP_200_OK, response_model=AdminSchema)
def get_admin(admin_id: int = Depends(is_autheticated), db: Session = Depends(get_db)):
    admin = Admin.get_admin_by_id(admin_id,db)
    if not admin:
        raise admin_not_found_exception
    return admin
