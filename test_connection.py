from db.mongo_connection import get_database

db = get_database()
print("¡Conexión a MongoDB exitosa!")

peliculas = db['peliculas']
resultado = peliculas.insert_one({"titulo": "Guerra Mundial Z", "anio": 2013, "genero": "Accion, Zombies"})

print("Documento insertado con ID:", resultado.inserted_id)
print("Colecciones disponibles:", db.list_collection_names())
