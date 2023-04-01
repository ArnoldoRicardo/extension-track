from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

metadata = MetaData()

events = Table('events', metadata,
    Column('id', Integer, primary_key=True),
    Column('nombre', String),
    Column('fecha', String),
    Column('ubicacion', String),
    Column('descripcion', String),
)

metadata.create_all(engine)


engine = create_engine('sqlite:///eventos.db')
