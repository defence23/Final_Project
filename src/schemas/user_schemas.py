from pydantic import BaseModel

class CarteBase(BaseModel):
    titlu: str
    autor: str
    isbn: str

class CarteCreate(CarteBase):
    pass

class Carte(CarteBase):
    id: int

    class Config:
        orm_mode = True
