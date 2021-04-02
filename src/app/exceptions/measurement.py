from fastapi import HTTPException
from fastapi import status


measurement_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Measurement does not exist",
)
