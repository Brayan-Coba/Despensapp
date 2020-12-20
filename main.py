from db.inventario_db import ProductosInDB
from db.inventario_db import update_producto, get_producto
from models.inventario_models import ProductosIn, ProductosOut
import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "https://despensapp-app.herokuapp.com/",
    "https://despensapp-app.herokuapp.com/user/inventario/tendero1", "https://despensapp-app.herokuapp.com/user/inventario/",
    "https://despensapp-app.herokuapp.com/user/inventario/Papa", "https://despensapp-app.herokuapp.com/user/inventario/tendero1",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.get("/inventario/{item}")
async def get_item(item: str):

    item_in_db = get_producto(item)

    if item_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")

    producto_out = ProductosOut(**item_in_db.dict())

    return  producto_out



@api.put("/inventario/actualizar_precio")
async def up_producto(productos_in : ProductosIn):
    producto_in_db = get_producto(productos_in.producto)
    
    if producto_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")


    producto_in_db.precio = productos_in.precio
    "update_producto(producto_in_db)"

    return producto_in_db
