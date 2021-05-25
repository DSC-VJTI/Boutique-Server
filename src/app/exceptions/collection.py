from fastapi import HTTPException
from fastapi import status

collection_already_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Collection with this title already exists",
)

collection_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Collection does not exist",
)
