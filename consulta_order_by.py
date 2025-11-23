# consulta_order_by.py
from configuracion import Session
from models import Publicacion
from sqlalchemy import desc

session = Session()

# Ordenar publicaciones por fecha (más recientes primero)
publicaciones = session.query(Publicacion).order_by(
    desc(Publicacion.fecha_publicacion)
).all()

print("=== PUBLICACIONES ORDENADAS POR FECHA DESCENDENTE ===")
for pub in publicaciones:
    print(pub)

session.close()
