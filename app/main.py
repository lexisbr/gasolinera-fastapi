from fastapi import Depends
from fastapi import FastAPI
import models, schemas
from Conexion import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

