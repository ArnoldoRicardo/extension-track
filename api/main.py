from fastapi import FastAPI
from db import engine, events
from google.main import service
from google.service import crear_evento

app = FastAPI()


class Event(BaseModel):
    nombre: str
    fecha: str
    ubicacion: Optional[str] = None
    descripcion: Optional[str] = None


@app.post("/calendar/")
async def recibir_eventos(event: Event):
    print(event)
    # validar que el evento no exista
    # si no existe, crearlo
    # si existe, actualizarlo
    with engine.connect() as conn:
        result = conn.execute(events.select().where(events.c.nombre == event.nombre))
        if result.rowcount == 0:
            conn.execute(events.insert().values(nombre=event.nombre, fecha=event.fecha, ubicacion=event.ubicacion, descripcion=event.descripcion))
            crear_evento(event.nombre, event.fecha, event.ubicacion, event.descripcion)
        else:
            conn.execute(events.update().where(events.c.nombre == event.nombre).values(nombre=event.nombre, fecha=event.fecha, ubicacion=event.ubicacion, descripcion=event.descripcion))
            actualizar_evento(event.nombre, event.fecha, event.ubicacion, event.descripcion)
    return {"mensaje": "Evento recibido"}
