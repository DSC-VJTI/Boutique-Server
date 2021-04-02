from fastapi import HTTPException
from fastapi import status


material_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Material does not exist",
)
