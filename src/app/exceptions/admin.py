from fastapi import HTTPException
from fastapi import status

token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token Expired",
    headers={"WWW-Authenticate": "Bearer"},
)

admin_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Admin does not exist",
)

incorrect_password_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect Password",
)

admin_already_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Admin already exists",
)
