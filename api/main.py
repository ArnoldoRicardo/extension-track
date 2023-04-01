from fastapi import FastAPI
from db import engine, events

app = FastAPI()


class Event(BaseModel):
    nombre: str
    fecha: str
    ubicacion: Optional[str] = None
    descripcion: Optional[str] = None


@app.post("/calendar/")
async def recibir_eventos(event: Event):
    print(event)
    with engine.connect() as conn:
        conn.execute(events.insert().values(nombre=event.nombre, fecha=event.fecha, ubicacion=event.ubicacion, descripcion=event.descripcion))
    return {"mensaje": "Evento recibido"}
