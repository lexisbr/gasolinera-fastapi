from sqlalchemy import Column, Integer, String, Float, ForeignKey;
from Conexion import Base;

class Estacion(Base):
    __tablename__ = "estacion";

    id_estacion = Column(Integer, primary_key=True, index=True);
    nombre = Column(String(100));

class Tanque(Base):
    __tablename__ = "tanque";

    id_tanque = Column(Integer, primary_key=True, index=True);
    id_estacion = Column(Integer, ForeignKey("estacion.id_estacion"));
    capacidad_galones = Column(Float);
    nivel_actual_galones = Column(Float);
    tipo_gasolina = Column(String(50));