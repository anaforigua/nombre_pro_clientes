from fastapi import APIRouter, HTTPException,status
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
    lista_facturas= sesion.exec(select(Factura)).all()
    return lista_facturas

#Listar una factura por ID
@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def obtener_factura(
    factura_id: int,
    mi_sesion: Sesion_dependencia
):
    factura_bd = mi_sesion.get(Factura, factura_id)

    if not factura_bd:
        raise HTTPException(
            status_code=404,
            detail=f"La factura con id {factura_id} no existe."
        )
    return factura_bd
    
#Crear una factura
@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion:Sesion_dependencia):
    
    
    cliente_encontrado = sesion.get(Cliente, cliente_id)


    if not cliente_encontrado:
        raise HTTPException(
            status_code=400,
            detail=f"El cliente con id {cliente_id} no existe."
        )
    
    factura_dict= datos_factura.model_dump()
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
async def editar_factura(factura_id: int,datos_factura: FacturaEditar, mi_sesion: Sesion_dependencia):
    factura_bd = mi_sesion.get(Factura, factura_id)

    if not factura_bd:
        raise HTTPException(
            status_code=404,
            detail=f"La factura con id {factura_id} no existe."
        )
    factura_dict = datos_factura.model_dump(exclude_unset=True)
    factura_bd.sqlmodel_update(factura_dict)

    mi_sesion.add(factura_bd)
    mi_sesion.commit()
    mi_sesion.refresh(factura_bd)
    return factura_bd

#eliminar factura
@rutas_facturas.delete("/facturas/{factura_id}", response_model= Cliente)
async def eliminar_factura(factura_id: int, mi_sesion: Sesion_dependencia):
    factura_bd = mi_sesion.get(Factura, factura_id)

    if not factura_bd:
        raise HTTPException(
            status_code=status .HTTP_404_NOT_FOUND,
            detail=f"La factura con id {factura_id} no existe."
        )

    mi_sesion.delete(factura_bd)
    mi_sesion.commit()

    return factura_bd
    
    


