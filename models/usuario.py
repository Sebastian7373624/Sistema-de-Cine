from db.mongo_connection import db

def crear_usuario(usuario):
    resultado = db.usuarios.insert_one(usuario)
    return resultado.inserted_id

def obtener_usuario_por_email(email):
    return db.usuarios.find_one({"email": email})

def actualizar_historial_compras(email, compra):
    db.usuarios.update_one(
        {"email": email},
        {"$push": {"historial_compras": compra}}
    )
