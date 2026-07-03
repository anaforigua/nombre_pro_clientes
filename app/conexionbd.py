from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine

nombre_bd = "bd_clientes.sqlte3"
url_bd = f"sqlite:///{nombre_bd}"

motor_bd = create_engine(url_bd)



def crear_tablas(app: FastAPI):
    # Ver las tablas registradas
    print(SQLModel.metadata.tables.keys())
    SQLModel.metadata.create_all(motor_bd)
    yield

def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion

Sesion_dependencia = Annotated[Session, Depends(obtener_sesion)]