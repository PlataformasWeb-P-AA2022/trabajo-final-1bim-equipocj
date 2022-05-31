from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Provincia, Canton #1
from configuracion import cadena_base_datos #2

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

provincia = [] 


with open ('data/Listado-Instituciones-Educativas.csv', 'r',encoding="utf8") as archivo:

    for r in archivo:
        r = r.split('|')
        provincia.append((r[2], r[3]))

for p in provincia:
    session.add(Provincia(codigoProvincia=p[0],nombreProvincia=p[1] ))
session.commit()