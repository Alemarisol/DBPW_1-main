from sqlalchemy import create_engine
from models import Base  # Esto importa mis modelos desde models.py

# Crear motor para SQLite
engine = create_engine("sqlite:///DBPW_001.db")

# Crear todas las tablas definidas en models.py
Base.metadata.create_all(engine)

print("Base de datos creada correctamente.")
