from pydantic import BaseModel


class MaterialBase(BaseModel):
    client_name: str
    top: str
    bottom: str
    dupatta: str
    lining: str

    laces: str
    emroidery: str
    piping: str
    zip: str
    buttons: str

    tailoring: str
    convayance: str
    overheads: str


class MaterialSchema(MaterialBase):
    id: int

    class Config:
        orm_mode = True
