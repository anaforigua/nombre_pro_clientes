from fastapi import APIRouter, HTTPException,status
from ..modelos.clientes import Cliente, ClienteCrear,ClienteEditar
from  ..listas import lista_clientes
from ..conexionbd import Sesion_dependencia
from sqlmodel import select

rutas_clientes=APIRouter()
#lista_clientes:list[Cliente] = []

@rutas_clientes.get("/clientes",response_model=list[Cliente])
async def listar_clientes(sesion:Sesion_dependencia):
    lista_clientes=sesion.exec(select(Cliente)).all()
    return lista_clientes

#endpoint listar un cliente
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_clientes(cliente_id:int, mi_sesion:Sesion_dependencia):
    cliente_bd =mi_sesion.get(Cliente,cliente_id)
    if not cliente_bd:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"El cliente con id {cliente_id} no existe."
    )
    return cliente_bd

 # ENDPOINT PARA CREAR CLIENTE Y AGREGA A LA LISTA      
@rutas_clientes.post("/clientes", response_model=Cliente)
async def  crear_cliente(datos_cliente: ClienteCrear, mi_sesion:Sesion_dependencia):
    cliente_val= Cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_val)
    return cliente_val

# ENDPOINT PARA EDITAR UN CLIENTE Y AGREGA A LA LISTA
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(
    cliente_id: int,
    datos_cliente: ClienteEditar,
    mi_sesion: Sesion_dependencia
):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)

    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id} no existe."
        )

    cliente_dict = datos_cliente.model_dump(exclude_unset=True)
    cliente_bd.sqlmodel_update(cliente_dict)

    mi_sesion.add(cliente_bd)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_bd)

    return cliente_bd

# ENDPOINT PARA ELIMINAR UN CLIENTE DE LA LISTA
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int, mi_sesion: Sesion_dependencia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)

    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id} no existe."
        )

    mi_sesion.delete(cliente_bd)
    mi_sesion.commit()

    return cliente_bd
   