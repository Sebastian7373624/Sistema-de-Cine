import tkinter as tk

def mostrar_admin_dashboard(usuario):
    admin_win = tk.Tk()
    admin_win.title(f"Panel Administrador - {usuario.get('nombre')}")

    tk.Label(admin_win, text="Bienvenido Administrador").pack()

    admin_win.mainloop()
