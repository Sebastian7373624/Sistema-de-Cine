from db.mongo_connection import db

def agregar_pelicula(pelicula):
    resultado = db.peliculas.insert_one(pelicula)
    return resultado.inserted_id

def obtener_pelicula_por_nombre(nombre):
    return db.peliculas.find_one({"nombre": nombre})

def actualizar_disponibilidad(nombre, cantidad):
    db.peliculas.update_one(
        {"nombre": nombre},
        {"$inc": {"disponibilidad": -cantidad}}
    )
