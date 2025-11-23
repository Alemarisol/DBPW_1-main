from configuracion import engine 
from models import Base

# Esto crea todas las tablas definidas en mis modelos
Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente.")
