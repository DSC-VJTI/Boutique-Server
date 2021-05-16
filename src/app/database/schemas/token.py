from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    is_admin: bool
