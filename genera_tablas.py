from contextlib import nullcontext
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigoAMIE = Column(String(100))
    nombre = Column(String(100))
    codigoDistrito = Column(String(50))
    sostenimiento = Column(String(100))
    tipoEducacion = Column(String(100))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    acceso = Column(String(50))
    nroEstudiantes = Column(Integer)
    nroDocentes = Column(Integer)

    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    parroquia = relationship("Parroquia", back_populates="establecimiento")

    
    def __repr__(self):
        return "Establecimiento: codigoAMIE=%s - nombre=%s - codigoDistrito=%s - sostenimiento=%s - \
        		tipoEducacion=%s - modalidad=%s - jornada=%s - acceso=%s - nroEstudiantes=%d - \
        		nroDocentes=%d " % (
                          self.codigoAMIE, 
                          self.nombre, 
                          self.codigoDistrito, 
                          self.sostenimiento,
                          self.tipoEducacion,
                          self.modalidad,
                          self.jornada,
                          self.acceso,
                          self.nroEstudiantes,
                          self.nroDocentes)

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigoProvincia = Column(String(50))
    nombreProvincia = Column(String(100))
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia: codigoProvincia=%s - nombreProvincia=%s "  % (
                          self.codigoProvincia, 
                          self.nombreProvincia)

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigoCanton = Column(String(50))
    nombreCanton = Column(String(100), nullable=False)
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    
    provincia = relationship("Provincia", back_populates="cantones")
    parroquia = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return "Canton: codigoCanton=%s - nombreCanton=%s " % (
                          self.codigoCanton, 
                          self.nombreCanton)

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigoParroquia = Column(String(50))
    nombreParroquia = Column(String(100))
    canton_id = Column(Integer, ForeignKey('canton.id'))
    
    canton  = relationship("Canton", back_populates="parroquia")
    establecimiento  = relationship("Establecimiento", back_populates="parroquia")
    
    def __repr__(self):
        return "Parroquia: codigoParroquia=%s - nombreParroquia=%s " % (
                self.codigoParroquia,
                self.nombreParroquia)

Base.metadata.create_all(engine)