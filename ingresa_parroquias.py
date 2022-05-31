from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Canton, Parroquia #1
from configuracion import cadena_base_datos #2

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

parroquias = [] 

with open ('data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for r in archivo:
        r = r.split('|')
        parroquias.append((r[6], r[7], r[4]))

for p in parroquias:
    c = session.query(Canton).filter_by(codigoCanton=p[2]).first()

    session.add(Parroquia(codigoParroquia=p[0],nombreParroquia=p[1],canton = c))
session.commit()