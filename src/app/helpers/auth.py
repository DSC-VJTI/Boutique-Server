import os
from datetime import datetime
from datetime import timedelta
from typing import Dict
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def create_access_token(data: Dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        os.environ.get("SECRET_KEY"),
        algorithm=os.environ.get("ALGORITHM"),
    )
    return encoded_jwt
