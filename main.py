from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente
from modelos.facturas import Factura
from modelos.transacciones import Transaccion, transacciones
app = FastAPI()


clientes: list[Cliente] = []
facturas: list[Factura] = []
transacciones: list[Transaccion] = []

# CRUD CLIENTES

@app.get("/clientes")
async def listar_clientes():
    return clientes

@app.get("/clientes/{id}")
async def obtener_cliente(id: int):
    for cliente in clientes:
        if cliente.id == id:
            return cliente
    raise HTTPException(404, "Cliente no encontrado")

@app.post("/clientes")
async def crear_cliente(cliente: Cliente):
    clientes.append(cliente)
    return {
        "mensaje": "Cliente creado",
        "cliente": cliente
    }

@app.put("/clientes/{id}")
async def actualizar_cliente(id: int, datos: Cliente):

    for i, cliente in enumerate(clientes):
        if cliente.id == id:
            clientes[i] = datos
            return {
                "mensaje": "Cliente actualizado",
                "cliente": datos
            }

    raise HTTPException(404, "Cliente no encontrado")

@app.delete("/clientes/{id}")
async def eliminar_cliente(id: int):

    for cliente in clientes:
        if cliente.id == id:
            clientes.remove(cliente)
            return {"mensaje": "Cliente eliminado"}

    raise HTTPException(404, "Cliente no encontrado")


# CRUD FACTURAS


@app.get("/facturas")
async def listar_facturas():
    return facturas

@app.post("/facturas")
async def crear_factura(factura: Factura):

    facturas.append(factura)

    return {
        "mensaje": "Factura creada",
        "factura": factura
    }

@app.get("/facturas/{id}")
async def obtener_factura(id: int):
#recorrer la lista
    for factura in facturas:
        if factura.id == id:
            return factura

    raise HTTPException(404, "Factura no encontrada")

@app.put("/facturas/{id}")
async def actualizar_factura(id: int, datos: Factura):

    for i, factura in enumerate(facturas):
        if factura.id == id:
            facturas[i] = datos
            return {
                "mensaje": "Factura actualizada",
                "factura": datos
            }

    raise HTTPException(404, "Factura no encontrada")

@app.delete("/facturas/{id}")
async def eliminar_factura(id: int):

    for factura in facturas:
        if factura.id == id:
            facturas.remove(factura)
            return {"mensaje": "Factura eliminada"}

    raise HTTPException(404, "Factura no encontrada")


# CRUD TRANSACCIONES


@app.get("/transacciones")
async def listar_transacciones():
    return transacciones

@app.post("/transacciones")
async def crear_transaccion(transaccion: Transaccion):

    transacciones.append(transaccion)

    return {
        "mensaje": "Transacción creada",
        "transaccion": transaccion
    }

@app.get("/transacciones/{id}")
async def obtener_transaccion(id: int):

    for transaccion in transacciones:
        if transaccion.id == id:
            return transaccion

    raise HTTPException(404, "Transacción no encontrada")

@app.put("/transacciones/{id}")
async def actualizar_transaccion(id: int, datos: Transaccion):

    for i, transaccion in enumerate(transacciones):
        if transaccion.id == id:
            transacciones[i] = datos
            return {
                "mensaje": "Transacción actualizada",
                "transaccion": datos
            }

    raise HTTPException(404, "Transacción no encontrada")

@app.delete("/transacciones/{id}")
async def eliminar_transaccion(id: int):

    for transaccion in transacciones:
        if transaccion.id == id:
            transacciones.remove(transaccion)
            return {"mensaje": "Transacción eliminada"}

    raise HTTPException(404, "Transacción no encontrada")