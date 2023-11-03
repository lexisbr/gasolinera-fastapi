from fastapi import Depends
from fastapi import FastAPI
import models, schemas
from Conexion import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/estacion/", response_model=List[schemas.Estacion])
async def get_estaciones(db: Session = Depends(get_db)):
    return db.query(models.Estacion).all()

@app.get("/estacion/{id_estacion}", response_model=schemas.Estacion)
async def get_estacion(id_estacion: int, db: Session = Depends(get_db)):
    return db.query(models.Estacion).filter(models.Estacion.id_estacion == id_estacion).first()

@app.post("/transaccion/")
async def post_transaccion(transaccion: schemas.TransaccionNoDetalladaDTO, db: Session = Depends(get_db)):
    galonesConsumidos = transaccion.galonesServidos
    idTanque = transaccion.idTanque

    tanque = db.query(models.Tanque).filter(models.Tanque.id_tanque == idTanque).first()

    if tanque.nivel_actual_galones < galonesConsumidos:
        return {"success":False, "message": "No hay suficiente combustible en el tanque"}
    else:
        tanque.nivel_actual_galones -= galonesConsumidos
        db.commit()
        db.refresh(tanque)

        new_transaccion = models.TransaccionNoDetallada(
            id_tanque=idTanque,
            id_cliente=transaccion.idCliente,
            tipo_pago=transaccion.tipoPago,
            galones_servidos=galonesConsumidos,
            fecha_transaccion=datetime.now()
        )

        # Add the new transaccion to the database session
        db.add(new_transaccion)
        db.commit()
        db.refresh(new_transaccion)

        return {"success":True, "message": "Transaccion realizada satisfactoriamente"}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

