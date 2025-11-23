# consulta_and.py
from configuracion import Session
from models import Investigador
from sqlalchemy import and_

session = Session()

# Investigadores llamados Skye y del área Matemáticas
resultado = session.query(Investigador).filter(
    and_(
        Investigador.nombre == "Skye",
        Investigador.area_investigacion == "Matemáticas"
    )
).all()

print("=== INVESTIGADORES LLAMADOS SKYE DEL ÁREA MATEMÁTICAS ===")
for inv in resultado:
    print(inv)

session.close()
