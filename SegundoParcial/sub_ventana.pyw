from tkinter import *

import tkinter as tk

def cuadro1():
    pass

def cuadro2():
    pass

def abrir_subventana():
    sub = tk.Toplevel(raiz)
    sub.title('Ventana Secundaria')
    tk.Label(sub, text='Esto es una subventana', font=('Comic Sans MS', 18)).pack()
    sub.geometry('800x500')
    opciones = [
        ('Cuadro1', cuadro1),
        ('Cuadro2', cuadro2),
        ('Cerrar', sub.destroy)
    ]

    for texto, funcion in opciones:
        tk.Button(sub, text=texto, width=25, height=5, command=funcion).pack(padx=20, pady=20)

raiz = Tk()
raiz.title('Ventana Principal')
raiz.config(bg='bisque3')
raiz.geometry('1000x800')
tk.Button(raiz, text='Abrir Ventana', width=25, height=5, command=abrir_subventana).pack()
raiz.mainloop()