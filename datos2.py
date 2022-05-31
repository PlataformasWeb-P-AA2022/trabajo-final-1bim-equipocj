from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

print("CONSULTA 1")
print("Las parroquias que tienen establecimientos únicamente en la jornada Matutina y Vespertina")

consulta5 = session.query(Parroquia).join(Establecimiento).filter(or_(Establecimiento.jornada == "Matutina",
	Establecimiento.jornada == "Vespertina")).all()

print("Presentación")
for c in consulta5:
    print("%s" % (c))
    print("---------")

print("___________________________________________________")

print("CONSULTA 2")
print("Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459")

consulta6 = session.query(Canton).join(Parroquia, Establecimiento).filter(or_(Establecimiento.nroEstudiantes == 448,
	Establecimiento.nroEstudiantes == 450, Establecimiento.nroEstudiantes == 451, Establecimiento.nroEstudiantes == 454,
	Establecimiento.nroEstudiantes == 458, Establecimiento.nroEstudiantes == 459)).all()

print("Presentación")
for c in consulta6:
    print("%s" % (c))
    print("---------")