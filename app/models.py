from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime;
from Conexion import Base;

class Cliente(Base):
    __tablename__ = "cliente";

    id_cliente = Column(Integer, primary_key=True, index=True);
    nit = Column(String(100));
    nombre = Column(String(100));
    puntos = Column(Integer);


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

class TransaccionNoDetallada(Base):
    __tablename__ = "transaccion_no_detallada";

    id_transaccion = Column(Integer, primary_key=True, index=True);
    id_tanque = Column(Integer, ForeignKey("tanque.id_tanque"));
    id_cliente = Column(Integer, ForeignKey("cliente.id_cliente"));
    tipo_pago = Column(String(50));
    galones_servidos = Column(Float);
    fecha_transaccion = Column(DateTime);