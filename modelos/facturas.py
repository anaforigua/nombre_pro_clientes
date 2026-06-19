from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Factura(BaseModel):
    id: int
    fecha: str
    total: float
    cliente_id: int
    
    # CRUD FACTURAS


@app.get("/facturas")
def listar_facturas():
    return facturas

@app.post("/facturas")
def crear_factura(factura: Factura):

    facturas.append(factura)

    return {
        "mensaje": "Factura creada",
        "factura": factura
    }

@app.get("/facturas/{id}")
def obtener_factura(id: int):

    for factura in facturas:
        if factura.id == id:
            return factura

    raise HTTPException(404, "Factura no encontrada")

@app.put("/facturas/{id}")
def actualizar_factura(id: int, datos: Factura):

    for i, factura in enumerate(facturas):
        if factura.id == id:
            facturas[i] = datos
            return {
                "mensaje": "Factura actualizada",
                "factura": datos
            }

    raise HTTPException(404, "Factura no encontrada")

@app.delete("/facturas/{id}")
def eliminar_factura(id: int):

    for factura in facturas:
        if factura.id == id:
            facturas.remove(factura)
            return {"mensaje": "Factura eliminada"}

    raise HTTPException(404, "Factura no encontrada")
