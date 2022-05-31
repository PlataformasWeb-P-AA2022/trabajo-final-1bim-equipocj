from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Canton, Provincia #1
from configuracion import cadena_base_datos #2

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

cantones = [] 

with open ('data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for r in archivo:
        r = r.split('|')
        cantones.append((r[4], r[5], r[2]))

for c in cantones:
    prov = session.query(Provincia).filter_by(codigoProvincia=c[2]).first()

    session.add(Canton(codigoCanton=c[0],nombreCanton=c[1],provincia = prov))
session.commit()
