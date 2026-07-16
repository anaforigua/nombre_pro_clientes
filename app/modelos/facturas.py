from pydantic import computed_field
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from .transacciones import Transaccion
from .clientes import Cliente, ClienteLeer


# BASE (NO ES TABLA)
class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)


# TABLA REAL (SOLO UNA VEZ)
class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")

    cliente: Cliente = Relationship(back_populates="factura")
    transacciones: list["Transaccion"] = Relationship(back_populates="factura")

    @computed_field
    @property
    def vr_total(self) -> float:
        total = 0.0

        if not self.transacciones:
            return total

        for t in self.transacciones:
            total += t.vr_unitario * t.cantidad

        return total


# DTOs
class FacturaCrear(FacturaBase):
    cliente_id: int


class FacturaEditar(SQLModel):
    fecha: datetime | None = None
    cliente_id: int | None = None


class FacturaEliminar(SQLModel):
    pass


class FacturaLeer(FacturaBase):
    id: int
    cliente: ClienteLeer


class FacturaLeerCompuesta(FacturaLeer):
    transacciones: list[Transaccion] = []
    vr_total: float
