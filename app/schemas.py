from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int
    nit: str
    nombre: str
    puntos: int

    class Config:
        from_attributes = True

class Estacion(BaseModel):
    id_estacion: int
    nombre: str

    class Config:
        from_attributes = True

class Tanque(BaseModel):
    id_tanque: int
    id_estacion: int
    capacidad_galones: float
    nivel_actual_galones: float
    tipo_gasolina: str

    class Config:
        from_attributes = True

class TransaccionNoDetallada(BaseModel):
    id_transaccion: int
    id_tanque: int
    id_cliente: int
    tipo_pago: str
    galones_servidos: float
    fecha_transaccion: str

    class Config:
        from_attributes = True

class TransaccionNoDetalladaDTO(BaseModel):
    idTanque: int
    idCliente: int
    tipoPago: str
    galonesServidos: float