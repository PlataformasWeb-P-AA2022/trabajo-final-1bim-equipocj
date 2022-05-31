from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

print("CONSULTA 1")
print("Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores")

consulta11 = session.query(Establecimiento).filter(Establecimiento.nroDocentes > 100).order_by(Establecimiento.nroEstudiantes).all()

print("Presentación")
for c in consulta11:
    print("%s" % (c))
    print("---------")

print("___________________________________________________")

print("CONSULTA 2")
print("Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores")

consulta12 = session.query(Establecimiento).filter(Establecimiento.nroDocentes > 100).order_by(Establecimiento.nroDocentes).all()

print("Presentación")
for c in consulta12:
    print("%s" % (c))
    print("---------")