from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

print("CONSULTA 1")
print("Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena\
 'Educación regular' en tipo de educación")

consulta9 = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.nroDocentes == 40,
	Establecimiento.tipoEducacion.like('Educación regular'))).order_by(Parroquia.nombreParroquia).all()

print("Presentación")
for c in consulta9:
    print("%s" % (c))
    print("---------")

print("___________________________________________________")

print("CONSULTA 2")
print("Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04")

consulta10 = session.query(Establecimiento).filter(Establecimiento.codigoDistrito.like('11D04')).order_by(Establecimiento.sostenimiento).all()

print("Presentación")
for c in consulta10:
    print("%s" % (c))
    print("---------")