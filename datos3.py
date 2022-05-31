from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

print("CONSULTA 1")
print("Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11 profesores")

consulta7 = session.query(Canton).join(Parroquia, Establecimiento).filter(or_(Establecimiento.nroDocentes == 0,
	Establecimiento.nroDocentes == 5, Establecimiento.nroDocentes == 11)).all()

print("Presentación")
for c in consulta7:
    print("%s" % (c))
    print("---------")

print("___________________________________________________")

print("CONSULTA 2")
print("Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21")

consulta8 = session.query(Establecimiento).join(Parroquia).filter(and_(Parroquia.nombreParroquia == "PINDAL",
	Establecimiento.nroEstudiantes >= 21)).all()

print("Presentación")
for c in consulta8:
    print("%s" % (c))
    print("---------")