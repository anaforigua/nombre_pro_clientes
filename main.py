from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Este es el proyecto de clientes a desarrollar"}

@app.get("/clientes")
def  clientes():
    clientes= ["Ana", "Edward", "Johanna", "Shakira","Maluma"]
    return {"mensaje":clientes }