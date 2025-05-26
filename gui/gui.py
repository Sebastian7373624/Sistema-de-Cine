import tkinter as tk
from tkinter import messagebox
from models.usuario import crear_usuario, obtener_usuario_por_email, actualizar_historial_compras
from models.peliculas import obtener_pelicula_por_nombre, agregar_pelicula, obtener_todas_peliculas, actualizar_disponibilidad
from models.transaccion import registrar_transaccion

class CineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Cine - Gestión")

      
        frame_usuario = tk.LabelFrame(root, text="Registrar Usuario")
        frame_usuario.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_usuario, text="Nombre:").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(frame_usuario)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(frame_usuario, text="Email:").grid(row=1, column=0)
        self.email_entry = tk.Entry(frame_usuario)
        self.email_entry.grid(row=1, column=1)

        tk.Button(frame_usuario, text="Registrar", command=self.registrar_usuario).grid(row=2, column=0, columnspan=2, pady=5)

     
        frame_peliculas = tk.LabelFrame(root, text="Películas Disponibles")
        frame_peliculas.pack(fill="x", padx=10, pady=5)

        self.peliculas_listbox = tk.Listbox(frame_peliculas, width=60)
        self.peliculas_listbox.pack()

        tk.Button(frame_peliculas, text="Actualizar lista", command=self.cargar_peliculas).pack(pady=5)

     
        frame_compra = tk.LabelFrame(root, text="Comprar Entradas")
        frame_compra.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_compra, text="Email usuario:").grid(row=0, column=0)
        self.compra_email_entry = tk.Entry(frame_compra)
        self.compra_email_entry.grid(row=0, column=1)

        tk.Label(frame_compra, text="Película (nombre exacto):").grid(row=1, column=0)
        self.compra_pelicula_entry = tk.Entry(frame_compra)
        self.compra_pelicula_entry.grid(row=1, column=1)

        tk.Label(frame_compra, text="Cantidad de entradas:").grid(row=2, column=0)
        self.compra_cantidad_entry = tk.Entry(frame_compra)
        self.compra_cantidad_entry.grid(row=2, column=1)

        tk.Button(frame_compra, text="Comprar", command=self.comprar_entradas).grid(row=3, column=0, columnspan=2, pady=5)

        # Cargar películas al inicio
        self.cargar_peliculas()

    def registrar_usuario(self):
        nombre = self.nombre_entry.get().strip()
        email = self.email_entry.get().strip()
        if not nombre or not email:
            messagebox.showerror("Error", "Debe ingresar nombre y email.")
            return
        # Intentar crear usuario
        try:
            crear_usuario({"nombre": nombre, "email": email, "historial_compras": [], "preferencias": []})
            messagebox.showinfo("Éxito", f"Usuario {nombre} registrado.")
            self.nombre_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar usuario: {str(e)}")

    def cargar_peliculas(self):
        self.peliculas_listbox.delete(0, tk.END)
        peliculas = obtener_todas_peliculas()
        for p in peliculas:
            texto = f"{p['nombre']} - Género: {p['genero']} - Horario: {p['horario']} - Entradas disponibles: {p['disponibilidad']}"
            self.peliculas_listbox.insert(tk.END, texto)

    def comprar_entradas(self):
        email = self.compra_email_entry.get().strip()
        pelicula_nombre = self.compra_pelicula_entry.get().strip()
        try:
            cantidad = int(self.compra_cantidad_entry.get())
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")
            return

        if not email or not pelicula_nombre or cantidad <= 0:
            messagebox.showerror("Error", "Complete todos los campos correctamente.")
            return

        pelicula = obtener_pelicula_por_nombre(pelicula_nombre)
        if not pelicula:
            messagebox.showerror("Error", "Película no encontrada.")
            return

        if pelicula['disponibilidad'] < cantidad:
            messagebox.showerror("Error", "No hay entradas suficientes disponibles.")
            return

      
        actualizar_disponibilidad(pelicula_nombre, cantidad)

        
        compra = {"pelicula": pelicula_nombre, "cantidad": cantidad}
        actualizar_historial_compras(email, compra)

        # Registrar transacción
        recibo = {
            "usuario": email,
            "pelicula": pelicula_nombre,
            "cantidad": cantidad,
            "total": cantidad * 10  # Precio fijo por entrada
        }
        registrar_transaccion(recibo)

        messagebox.showinfo("Compra exitosa", f"Compra realizada:\n{recibo}")

        # Limpiar campos
        self.compra_email_entry.delete(0, tk.END)
        self.compra_pelicula_entry.delete(0, tk.END)
        self.compra_cantidad_entry.delete(0, tk.END)

        self.cargar_peliculas()

if __name__ == "__main__":
    root = tk.Tk()
    app = CineApp(root)
    root.mainloop()
