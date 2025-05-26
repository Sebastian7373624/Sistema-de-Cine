from db.mongo_connection import db
from datetime import datetime

def registrar_transaccion(transaccion):
    transaccion['fecha'] = datetime.now()
    resultado = db.transacciones.insert_one(transaccion)
    return resultado.inserted_id
