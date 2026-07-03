from pydantic import BaseModel
from modelos.clientes import Cliente
class Factura(BaseModel):
    id_factura: int
    fecha: str
    total: float
    cliente_id:Cliente
facturas = [] 

