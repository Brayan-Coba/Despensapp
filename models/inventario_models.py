from pydantic import BaseModel

class ProductosIn(BaseModel):
    producto: str
    precio: int


class ProductosOut(BaseModel):
    producto: str
    precio: int
    cantidad: int
    unidad: str
