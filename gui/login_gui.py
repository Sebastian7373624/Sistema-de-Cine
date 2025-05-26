import tkinter as tk
from tkinter import messagebox
from models.usuario import obtener_usuario_por_email
from gui.admin_dashboard import mostrar_admin_dashboard
from gui.user_dashboard import mostrar_user_dashboard

def login():
    email = entry_email.get()
    password = entry_password.get()

    usuario = obtener_usuario_por_email(email)
    if usuario and usuario.get("password") == password:
        root.destroy()
        if usuario.get("rol") == "admin":
            mostrar_admin_dashboard(usuario)
        else:
            mostrar_user_dashboard(usuario)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

root = tk.Tk()
root.title("Login Sala de Cine")

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Contraseña:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_login = tk.Button(root, text="Iniciar sesión", command=login)
btn_login.pack()

root.mainloop()
