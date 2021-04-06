from fastapi import HTTPException
from fastapi import status

category_already_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Category with this name already exists",
)

category_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Category does not exist",
)

sub_category_already_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Sub category with this name already exists",
)

sub_category_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Sub category does not exist",
)
