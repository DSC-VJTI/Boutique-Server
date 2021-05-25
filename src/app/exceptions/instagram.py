from fastapi import HTTPException
from fastapi import status

image_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Image does not exist",
)
