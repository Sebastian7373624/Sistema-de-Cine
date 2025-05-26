from models.usuario import crear_usuario
from models.peliculas import agregar_pelicula, obtener_pelicula_por_nombre, actualizar_disponibilidad
from models.transaccion import registrar_transaccion
from datetime import datetime

# Crear usuarios
usuarios = [
    {"nombre": "Ana", "email": "ana@mail.com", "historial_compras": [], "preferencias": []},
    {"nombre": "Luis", "email": "luis@mail.com", "historial_compras": [], "preferencias": []},
    {"nombre": "Marta", "email": "marta@mail.com", "historial_compras": [], "preferencias": []},
]

for usuario in usuarios:
    crear_usuario(usuario)
print("Usuarios creados.")

# Agregar películas
peliculas = [
    {"nombre": "La Gran Aventura Lego", "genero": "Animación", "duracion": 100, "horario": "18:00", "disponibilidad": 50},
    {"nombre": "Son como niños", "genero": "Comedia", "duracion": 110, "horario": "20:00", "disponibilidad": 40},
    {"nombre": "Smile", "genero": "Terror", "duracion": 95, "horario": "22:00", "disponibilidad": 30},
]

for pelicula in peliculas:
    agregar_pelicula(pelicula)
print("Películas agregadas.")

# Simular compras
compras = [
    {"usuario_email": "ana@mail.com", "pelicula": "La Gran Aventura Lego", "cantidad": 3},
    {"usuario_email": "luis@mail.com", "pelicula": "Son como niños", "cantidad": 2},
    {"usuario_email": "marta@mail.com", "pelicula": "Smile", "cantidad": 1},
    {"usuario_email": "ana@mail.com", "pelicula": "Son como niños", "cantidad": 1},
    {"usuario_email": "luis@mail.com", "pelicula": "La Gran Aventura Lego", "cantidad": 4},
]

for compra in compras:
    pelicula = obtener_pelicula_por_nombre(compra["pelicula"])
    if pelicula and pelicula["disponibilidad"] >= compra["cantidad"]:
        # Actualizar disponibilidad
        actualizar_disponibilidad(compra["pelicula"], compra["cantidad"])
        
        # Actualizar historial de compras usuario
        from models.usuario import actualizar_historial_compras
        actualizar_historial_compras(compra["usuario_email"], {
            "pelicula": compra["pelicula"],
            "cantidad": compra["cantidad"],
            "fecha": datetime.now()
        })
        
        # Registrar transacción
        total = compra["cantidad"] * 10  # Precio fijo 10 por entrada
        recibo = {
            "usuario": compra["usuario_email"],
            "pelicula": compra["pelicula"],
            "cantidad": compra["cantidad"],
            "total": total,
            "fecha": datetime.now()
        }
        registrar_transaccion(recibo)
        print(f"Compra realizada: {recibo}")
    else:
        print(f"No hay disponibilidad suficiente para {compra['pelicula']}")

