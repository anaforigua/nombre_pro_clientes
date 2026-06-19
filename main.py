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

@app.get("/clientes/{id_cliente}")
async def obtener_cliente(id_cliente: int):
    for cliente in clientes:
        if cliente.id == id_cliente:
            return cliente
    raise HTTPException(404, "Cliente no encontrado")

@app.post("/clientes")
def crear_cliente(cliente: Cliente):

    for c in clientes:
        if c.id == cliente.id:
            raise HTTPException(400, "El cliente ya existe")

    clientes.append(cliente)

    return {
        "mensaje": "Cliente creado",
        "cliente": cliente
    }

@app.put("/clientes/{id_cliente}")
async def actualizar_cliente(id_cliente: int, datos: Cliente):

    for i, cliente in enumerate(clientes):
        if cliente.id == id_cliente:
            clientes[i] = datos
            return {
                "mensaje": "Cliente actualizado",
                "cliente": datos
            }

    raise HTTPException(404, "Cliente no encontrado")

@app.delete("/clientes/{id_cliente}")
async def eliminar_cliente(id_cliente: int):

    for cliente in clientes:
        if cliente.id == id_cliente:
            clientes.remove(cliente)
            return {"mensaje": "Cliente eliminado"}

    raise HTTPException(404, "Cliente no encontrado")


# CRUD FACTURAS


@app.get("/facturas")
async def listar_facturas():
    return facturas

@app.post("/facturas")
def crear_factura(factura: Factura):

    for f in facturas:
        if f.id == factura.id:
            raise HTTPException(400, "La factura ya existe")

    facturas.append(factura)

    return {
        "mensaje": "Factura creada",
        "factura": factura
    }
    
@app.get("/facturas/{id_factura}")
async def obtener_factura(id_factura: int):
#recorrer la lista
    for factura in facturas:
        if factura.id == id_factura:
            return factura

    raise HTTPException(404, "Factura no encontrada")

@app.put("/facturas/{id_factura}")
async def actualizar_factura(id_factura: int, datos: Factura):

    for i, factura in enumerate(facturas):
        if factura.id == id_factura:
            facturas[i] = datos
            return {
                "mensaje": "Factura actualizada",
                "factura": datos
            }

    raise HTTPException(404, "Factura no encontrada")

@app.delete("/facturas/{id_factura}")
async def eliminar_factura(id_factura: int):

    for factura in facturas:
        if factura.id == id_factura:
            facturas.remove(factura)
            return {"mensaje": "Factura eliminada"}

    raise HTTPException(404, "Factura no encontrada")


# CRUD TRANSACCIONES


@app.get("/transacciones")
async def listar_transacciones():
    return transacciones

@app.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):

    for t in transacciones:
        if t.id == transaccion.id:
            raise HTTPException(400, "La transacción ya existe")

    transacciones.append(transaccion)

    return {
        "mensaje": "Transacción creada",
        "transaccion": transaccion
    }
    
@app.get("/transacciones/{id_transaccion}")
async def obtener_transaccion(id_transaccion: int):

    for transaccion in transacciones:
        if transaccion.id == id_transaccion:
            return transaccion

    raise HTTPException(404, "Transacción no encontrada")

@app.put("/transacciones/{id_transaccion}")
async def actualizar_transaccion(id_transaccion: int, datos: Transaccion):

    for i, transaccion in enumerate(transacciones):
        if transaccion.id == id_transaccion:
            transacciones[i] = datos
            return {
                "mensaje": "Transacción actualizada",
                "transaccion": datos
            }

    raise HTTPException(404, "Transacción no encontrada")

@app.delete("/transacciones/{id_transaccion}")
async def eliminar_transaccion(id_transaccion: int):

    for transaccion in transacciones:
        if transaccion.id == id_transaccion:
            transacciones.remove(transaccion)
            return {"mensaje": "Transacción eliminada"}

    raise HTTPException(404, "Transacción no encontrada")