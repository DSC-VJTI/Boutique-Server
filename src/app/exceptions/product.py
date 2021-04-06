from fastapi import HTTPException
from fastapi import status

product_already_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Product with this name already exists",
)

product_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Product does not exist",
)
