import tkinter as tk

def mostrar_user_dashboard(usuario):
    user_win = tk.Tk()
    user_win.title(f"Panel Usuario - {usuario.get('nombre')}")

    tk.Label(user_win, text=f"Bienvenido {usuario.get('nombre')}").pack()

    user_win.mainloop()
