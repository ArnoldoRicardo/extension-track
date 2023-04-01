from datetime import datetime, timedelta
from pytz import timezone
from googleapiclient.errors import HttpError

def crear_evento(service, nombre, fecha, ubicacion=None, descripcion=None):
    evento = {
        'summary': nombre,
        'location': ubicacion,
        'description': descripcion,
        'start': {
            'dateTime': fecha.isoformat(),
            'timeZone': timezone('America/Mexico_City').zone,
        },
        'end': {
            'dateTime': (fecha + timedelta(hours=1)).isoformat(),
            'timeZone': timezone('America/Mexico_City').zone,
        },
    }

    try:
        evento_creado = service.events().insert(calendarId='primary', body=evento).execute()
        print(f'Evento creado: {evento_creado.get("htmlLink")}')
    except HttpError as error:
        print(f'Ocurrió un error al crear el evento: {error}')

