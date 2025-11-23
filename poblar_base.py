from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Institucion, Departamento, Investigador, Publicacion
from datetime import datetime

# Conectar a la base de datos
engine = create_engine("sqlite:///DBPW_001.db")
Session = sessionmaker(bind=engine)
session = Session()

# Crear una institución
inst1 = Institucion(nombre="Universidad UTPL", ciudad="Ciudad LOJA", pais="Ecuador 123")
session.add(inst1)
session.commit()

# Crear un departamento
dept1 = Departamento(nombre="Departamento de Ciencias", codigo="DC01", institucion=inst1)
session.add(dept1)
session.commit()

# Crear un investigador
inv1 = Investigador(nombre="Skye", apellido="Moreno", email="ana.perez@example.com", area_investigacion="Biología", departamento=dept1)
session.add(inv1)
session.commit()

# Crear una publicación
pub1 = Publicacion(
    titulo="Estudio sobre células",
    fecha_publicacion=datetime.strptime("2025-01-15", "%Y-%m-%d").date(),
    doi="10.1234/abcd.2025",
    tipo_publicacion="Artículo",
    investigador=inv1
)
session.add(pub1)
session.commit()

print("Datos insertados correctamente.")
