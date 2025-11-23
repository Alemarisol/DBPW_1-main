from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# ----------------------------------
# INSTITUCION
# ----------------------------------
class Institucion(Base):

    __tablename__ = "instituciones"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    pais = Column(String, nullable=False)

    departamentos = relationship("Departamento", back_populates="institucion")

    def __repr__(self):
        return "Institución: nombre=%s ciudad=%s país=%s" % (
            self.nombre,
            self.ciudad,
            self.pais
        )


# ----------------------------------
# DEPARTAMENTO
# ----------------------------------
class Departamento(Base):

    __tablename__ = "departamentos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    codigo = Column(String, nullable=False)

    institucion_id = Column(Integer, ForeignKey("instituciones.id"), nullable=False)
    institucion = relationship("Institucion", back_populates="departamentos")

    investigadores = relationship("Investigador", back_populates="departamento")

    def __repr__(self):
        return "Departamento: nombre=%s código=%s institución=%s" % (
            self.nombre,
            self.codigo,
            self.institucion.nombre if self.institucion else None
        )


# ----------------------------------
# INVESTIGADOR
# ----------------------------------
class Investigador(Base):

    __tablename__ = "investigadores"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, nullable=False)
    area_investigacion = Column(String, nullable=False)

    departamento_id = Column(Integer, ForeignKey("departamentos.id"), nullable=False)
    departamento = relationship("Departamento", back_populates="investigadores")

    publicaciones = relationship("Publicacion", back_populates="investigador")

    def __repr__(self):
        return "Investigador: %s %s, área=%s, departamento=%s" % (
            self.nombre,
            self.apellido,
            self.area_investigacion,
            self.departamento.nombre if self.departamento else None
        )


# ----------------------------------
# PUBLICACION
# ----------------------------------
class Publicacion(Base):

    __tablename__ = "publicaciones"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    doi = Column(String, nullable=False)
    tipo_publicacion = Column(String, nullable=False)

    investigador_id = Column(Integer, ForeignKey("investigadores.id"), nullable=False)
    investigador = relationship("Investigador", back_populates="publicaciones")

    def set_fecha_from_string(self, fecha_str):
        self.fecha_publicacion = datetime.strptime(fecha_str, "%Y-%m-%d").date()

    def __repr__(self):
        return "Publicación: título=%s fecha=%s investigador=%s" % (
            self.titulo,
            self.fecha_publicacion,
            (self.investigador.nombre + ' ' + self.investigador.apellido)
            if self.investigador else None
        )

