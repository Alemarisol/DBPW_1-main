from configuracion import Session
from models import Investigador

session = Session()

# Obtener todos los investigadores
investigadores = session.query(Investigador).all()

print("=== TODOS LOS INVESTIGADORES ===")
for inv in investigadores:
    print(inv)

session.close()
