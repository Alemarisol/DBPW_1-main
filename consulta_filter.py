# consulta_filter.py
from configuracion import Session
from models import Investigador

session = Session()

# Filtrar investigadores del área de Biología
resultado = session.query(Investigador).filter(
    Investigador.area_investigacion == "Biología"
).all()

print("=== INVESTIGADORES DEL ÁREA DE BIOLOGÍA ===")
for inv in resultado:
    print(inv)

session.close()
