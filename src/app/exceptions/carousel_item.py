from fastapi import HTTPException
from fastapi import status

carousel_item_already_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Carousel Item with this title already exists",
)

carousel_item_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Carousel Item does not exist",
)
