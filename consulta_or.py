# consulta_or.py
from configuracion import Session
from models import Investigador
from sqlalchemy import or_

session = Session()

# Investigadores de Física o Química
resultado = session.query(Investigador).filter(
    or_(
        Investigador.area_investigacion == "Física",
        Investigador.area_investigacion == "Química"
    )
).all()

print("=== INVESTIGADORES DE FÍSICA O QUÍMICA ===")
for inv in resultado:
    print(inv)

session.close()
