from fastapi import APIRouter, HTTPException
from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..modelos.facturas import Factura
from ..listas import lista_transacciones, lista_facturas
from ..conexionbd import Sesion_dependencia
from sqlmodel import select

rutas_transacciones=APIRouter()
#lista_transacciones:list[Transaccion] = []
#lista_facturas:list[Factura] = []


#endpoints transacciones

#listar
@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones(sesion: Sesion_dependencia):
    # consulta=select(Transaccion)
    # lista_transacciones=sesion.exec(consulta).all
    # return lista_transacciones
    return sesion.exec(select(Transaccion)).all()
#listar por id
@rutas_transacciones.get("/transacciones/{transaccion_id}", response_model=Transaccion)
async def listar_transaccion(transaccion_id: int):
    for obj_transaccion in lista_transacciones:
        if obj_transaccion.id == transaccion_id:
            return obj_transaccion

    raise HTTPException(
        status_code=404,
        detail=f"La transacción con id {transaccion_id} no existe."
    )
    
#crear
@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear, sesion: Sesion_dependencia):
    factura_encontrada= sesion.get(Factura, factura_id)

    if not factura_encontrada:
        raise HTTPException(
            status_code=404,
            detail=f"La factura con id {factura_id} no existe."
        )
    transaccion_dict=datos_transaccion.model_dump()
    transaccion_dict["factura_id"]= factura_id
    transaccion_val = Transaccion.model_validate(transaccion_dict)
    #guardar bd
    sesion.add(transaccion_val)
    sesion.commit()
    sesion.refresh(transaccion_val)
    return transaccion_val

#editar
@rutas_transacciones.patch("/transacciones/{transaccion_id}", response_model= Transaccion)
async def editar_transaccion( transaccion_id: int, datos_transaccion:Transaccion
):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == transaccion_id:
            transaccion_val = Transaccion.model_validate(
                datos_transaccion.model_dump()
            )
            transaccion_val.id = transaccion_id
            transaccion_val.id_factura = obj_transaccion.id_factura

            lista_transacciones[i] = transaccion_val

            return transaccion_val

    raise HTTPException(
        status_code=404,
        detail=f"La transacción con id {transaccion_id} no existe."
    )
#eliminar
@rutas_transacciones.delete("/transacciones/{transaccion_id}")
async def eliminar_transaccion(transaccion_id: int):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == transaccion_id:
            lista_transacciones.pop(i)

            return {
                "mensaje": f"La transacción con id {transaccion_id} fue eliminada correctamente."
            }

    raise HTTPException(
        status_code=404,
        detail=f"La transacción con id {transaccion_id} no existe."
    )
