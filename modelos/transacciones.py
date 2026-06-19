from pydantic import BaseModel
class Transaccion(BaseModel):
    id_transaccion: int
    metodo_pago: str
    monto: float  
    vr_unitario:float
transacciones = []