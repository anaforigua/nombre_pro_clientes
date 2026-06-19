from fastapi import FastAPI

app = FastAPI()


listar_clientes: list[cliente]=[]

@app.get("/")
def inicio():
    return {"mensaje": "Este es el proyecto de clientes a desarrollar"}

@app.get("/clientes")
def  clientes():
    clientes= ["Ana", "Edward", "Johanna", "Shakira","Maluma"]
    return {"mensaje":clientes }

@app.get("/clientes")
def listar_clientes():
    return clientes

@app.get("/clientes/{id}")
def obtener_cliente(id: int):
    for cliente in clientes:
        if cliente.id == id:
            return cliente
    raise HTTPException(404, "Cliente no encontrado")

@app.post("/clientes")
def crear_cliente(cliente: Cliente):
    clientes.append(cliente)
    return {
        "mensaje": "Cliente creado",
        "cliente": cliente
    }

@app.put("/clientes/{id}")
def actualizar_cliente(id: int, datos: Cliente):

    for i, cliente in enumerate(clientes):
        if cliente.id == id:
            clientes[i] = datos
            return {
                "mensaje": "Cliente actualizado",
                "cliente": datos
            }

    raise HTTPException(404, "Cliente no encontrado")

@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):

    for cliente in clientes:
        if cliente.id == id:
            clientes.remove(cliente)
            return {"mensaje": "Cliente eliminado"}

    raise HTTPException(404, "Cliente no encontrado")