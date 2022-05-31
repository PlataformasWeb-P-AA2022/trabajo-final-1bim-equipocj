from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Establecimiento, Parroquia #1
from configuracion import cadena_base_datos #2

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

establecimientos = [] 

with open ('data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:
    next(archivo, None)

    for r in archivo:
        r = r.split('|')
        establecimientos.append((r[0],r[1],r[8],r[9],r[10],r[11],r[12],r[13], r[14], r[15].replace('\n',''), r[6]))

for e in establecimientos:
    parr = session.query(Parroquia).filter_by(codigoParroquia=e[10]).first()

    session.add(Establecimiento(codigoAMIE=e[0], nombre=e[1], codigoDistrito=e[2],sostenimiento=e[3], \
    	tipoEducacion=e[4], modalidad=e[5], jornada=e[6], acceso=e[7],nroEstudiantes=int(e[8]), \
    	nroDocentes=int(e[9]), parroquia = parr))
session.commit()