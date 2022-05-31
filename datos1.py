from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

print("CONSULTA 1")
print("Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553")

consulta1 = session.query(Establecimiento, Parroquia).join(Parroquia).filter(Parroquia.codigoParroquia.like('110553')).all()

print("Presentación")
for c in consulta1:
    print("%s" % (c))
    print("---------")

print("___________________________________________________")

print("CONSULTA 2")
print("Todos los establecimientos de la provincia del Oro")

consulta2 = session.query(Establecimiento, Provincia, Canton, Parroquia).join(Establecimiento.parroquia,
	Parroquia.canton, Canton.provincia).filter(Provincia.nombreProvincia.like('EL ORO')).all()

print("Presentación")
for c in consulta2:
    print("%s" % (c))
    print("---------")

print("___________________________________________________")

print("CONSULTA 3")
print("Todos los establecimientos del cantón de Portovelo")

consulta3 = session.query(Establecimiento, Provincia, Canton, Parroquia).join(Establecimiento.parroquia,
	Parroquia.canton).filter(Canton.nombreCanton.like('PORTOVELO')).all()

print("Presentación")
for c in consulta3:
    print("%s" % (c))
    print("---------")

print("___________________________________________________")

print("CONSULTA 4")
print("Todos los establecimientos del cantón de Zamora")

consulta4 = session.query(Establecimiento, Provincia, Canton, Parroquia).join(Establecimiento.parroquia,
	Parroquia.canton).filter(Canton.nombreCanton.like('ZAMORA')).all()

print("Presentación")
for c in consulta4:
    print("%s" % (c))
    print("---------")
