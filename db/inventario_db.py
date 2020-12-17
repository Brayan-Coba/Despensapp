from typing import  Dict
from pydantic import BaseModel

kg = "Kg"
lib = "Lib"

class ProductosInDB(BaseModel):
    producto: str
    precio: int
    cantidad: int
    unidad: str

database_productos = Dict[str, ProductosInDB]

database_productos = {
    "Papa": ProductosInDB(**{"producto":"Papa",
                            "precio":500,
                            "cantidad":50,
                            "unidad":kg}),

    "Arroz": ProductosInDB(**{"producto":"Arroz",
                            "precio":1200,
                            "cantidad":200,
                            "unidad":lib}),

    "Cebolla": ProductosInDB(**{"producto":"Cebolla",
                            "precio":750,
                            "cantidad":15,
                            "unidad":kg}),
}

def get_producto(producto: str):
    if producto in database_productos.keys():
        return database_productos[producto]
    else:
        return None

def update_producto(producto_in_db: ProductosInDB):
    database_productos[producto_in_db.producto] = producto_in_db
    return producto_in_db