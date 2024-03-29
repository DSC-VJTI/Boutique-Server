from fastapi import HTTPException
from fastapi import status

blog_already_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Blog with this title already exists",
)

blog_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Blog does not exist",
)
