from pydantic import BaseModel
from clientes import Cliente
class Factura(BaseModel):
    id: int
    fecha: str
    total: float
    cliente_id:Cliente
    

