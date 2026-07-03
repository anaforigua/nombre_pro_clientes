from fastapi import APIRouter, HTTPException
from ..modelos.facturas import Factura, FacturaCrear,FacturaEditar, FacturaLeer,FacturaLeerCompuesta
from ..modelos.clientes import Cliente, ClienteLeer
from ..listas import lista_clientes, lista_facturas
from ..conexionbd import Sesion_dependencia
from sqlmodel import select

rutas_facturas=APIRouter()
#lista_facturas:list[Factura] = []
#lista_clientes:list[Cliente] = []


#listar factura
@rutas_facturas.get("/facturas", response_model=list[FacturaLeerCompuesta])
async def listar_facturas(sesion:Sesion_dependencia):
    #select*from
    consulta=select(Factura)
        
    return lista_facturas

#Listar una factura por ID
@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def obtener_factura(factura_id: int):
    for obj_factura in lista_facturas:
        if obj_factura.id == factura_id:
            return obj_factura

    raise HTTPException(
        status_code=404,
        detail=f"La factura con id {factura_id} no existe."
    )
    
#Crear una factura
@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion:Sesion_dependencia):
    
    
    cliente_encontrado = sesion.get(Cliente, cliente_id)


    if not cliente_encontrado:
        raise HTTPException(
            status_code=400,
            detail=f"El cliente con id {cliente_id} no existe."
        )
    
    factura_dict= datos_factura.model_dump
    factura_dict["cliente_id"]=cliente_id
    factura_val = Factura.model_validate(factura_dict)
    factura_val.cliente = cliente_encontrado
    #guardar en bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val
#editar una factura
@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: FacturaEditar):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            factura_val = Factura.model_validate(datos_factura.model_dump())
            factura_val.id = factura_id
            lista_facturas[i] = factura_val
            return factura_val

    raise HTTPException(
        status_code=404,
        detail=f"La factura con id {factura_id} no existe."
    )
    
#eliminar factura
@rutas_facturas.delete("/facturas/{factura_id}")
async def eliminar_factura(factura_id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            lista_facturas.pop(i)
            return {
                "mensaje": f"La factura con id {factura_id} fue eliminada correctamente."
            }

    raise HTTPException(
        status_code=404,
        detail=f"La factura con id {factura_id} no existe."
    )


