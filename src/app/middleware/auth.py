import os

from database.db import get_db
from exceptions.admin import token_exception
from fastapi import Depends
from fastapi import Header
from jose import jwt
from jose import JWTError
from sqlalchemy.orm import Session


async def is_authenticated(
    authorization: str = Header(...), db: Session = Depends(get_db)
):
    token: str = authorization.split()[-1]
    try:
        payload = jwt.decode(
            token,
            os.environ.get("SECRET_KEY"),
            algorithms=os.environ.get("ALGORITHM"),
        )
        return payload.get("id")
    except JWTError:
        raise token_exception
