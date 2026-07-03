from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .facturas import Factura
#crear modelo transacciones con id cantidad,vr unitario,id factura
class TransaccionBase(SQLModel):
    cantidad: int = Field(default=0)
    vr_unitario: float = Field(default=0.0)


class TransaccionCrear(TransaccionBase):
    pass

class TransaccionEditar(TransaccionBase):
    pass

class TransaccionEliminar(TransaccionBase):
    pass

class Transaccion(TransaccionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura_id: int | None = Field(default=None, foreign_key="factura.id")
    factura:list["Factura"]=Relationship(back_populates="cliente")
    factura: "Factura" = Relationship(back_populates="transacciones")
    
class TransaccionLeer(TransaccionBase):
    id:int
    