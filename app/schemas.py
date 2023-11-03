from pydantic import BaseModel

class Estacion(BaseModel):
    id_estacion: int
    nombre: str

    class Config:
        orm_mode = True

class Tanque(BaseModel):
    id_tanque: int
    id_estacion: int
    capacidad_galones: float
    nivel_actual_galones: float
    tipo_gasolina: str

    class Config:
        orm_mode = True