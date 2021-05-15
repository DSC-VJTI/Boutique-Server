from exceptions.admin import sub_admin_exception
from exceptions.admin import token_exception
from fastapi import Header
from fastapi.exceptions import HTTPException
from helpers.auth import get_field_from_token
from jose import JWTError


async def is_authenticated(authorization: str = Header(...)):
    token: str = authorization.split()[-1]
    try:
        return get_field_from_token(token, "id")
    except JWTError:
        raise token_exception


async def is_admin(authorization: str = Header(...)):
    token: str = authorization.split()[-1]
    try:
        admin = get_field_from_token(token, "is_admin")
        if admin:
            return admin
        raise sub_admin_exception
    except HTTPException:
        raise sub_admin_exception
    except JWTError:
        raise token_exception
