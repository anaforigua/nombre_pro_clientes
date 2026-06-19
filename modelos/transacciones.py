from pydantic import BaseModel
class Transaccion(BaseModel):
    id: int
    metodo_pago: str
    monto: float  
    vr_unitario:float