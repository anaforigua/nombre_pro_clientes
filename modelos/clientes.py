from pydantic import BaseModel
class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    correo: str
    descripcion: str
clientes = []