



# CRUD TRANSACCIONES


@app.get("/transacciones")
def listar_transacciones():
    return transacciones

@app.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):

    transacciones.append(transaccion)

    return {
        "mensaje": "Transacción creada",
        "transaccion": transaccion
    }

@app.get("/transacciones/{id}")
def obtener_transaccion(id: int):

    for transaccion in transacciones:
        if transaccion.id == id:
            return transaccion

    raise HTTPException(404, "Transacción no encontrada")

@app.put("/transacciones/{id}")
def actualizar_transaccion(id: int, datos: Transaccion):

    for i, transaccion in enumerate(transacciones):
        if transaccion.id == id:
            transacciones[i] = datos
            return {
                "mensaje": "Transacción actualizada",
                "transaccion": datos
            }

    raise HTTPException(404, "Transacción no encontrada")

@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):

    for transaccion in transacciones:
        if transaccion.id == id:
            transacciones.remove(transaccion)
            return {"mensaje": "Transacción eliminada"}

    raise HTTPException(404, "Transacción no encontrada")

