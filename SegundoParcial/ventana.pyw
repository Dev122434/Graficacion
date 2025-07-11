from tkinter import *

from tkinter import ttk, messagebox
import sqlite3


def conectar() -> None:
    return sqlite3.connect('Prueba.db')

def registro_clientes() -> None:
    def mostrar_clientes() -> None:
        for renglon in tabla.get_children():
            tabla.delete(renglon)

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM Clientes')

        for fila in cursor.fetchall():
            tabla.insert('', END, values=fila)


        conexion.commit()
        conexion.close()

    vtn_clientes = Toplevel()
    vtn_clientes.title('Ventana Secundaria')
    vtn_clientes.geometry('800x500')


    ibl_titulo = Label(vtn_clientes, text='Esto es una subventana', font=('Comic Sans MS', 18))
    ibl_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=10)
    btn_cerrar = Button(vtn_clientes, text='Cerrar', command=vtn_clientes.destroy)
    btn_cerrar.grid(row=6, column=4, sticky='e', padx=10, pady=10)

    cols = ('Clave', 'Nombre', 'Genero', 'Codigo Postal')
    tabla = ttk.Treeview(vtn_clientes, columns=cols, show='headings')
    for col in cols:
        tabla.heading(col, text=col)
    tabla.grid(row=8, column=0, sticky='e', padx=5, pady=5, columnspan=10)

    mostrar_clientes()


raiz = Tk()
raiz.title('Ventana Principal')
raiz.config(bg='gray')
raiz.geometry('1000x800')

mi_frame = Frame(raiz, bg='red', width='650', height='500', pady=20, padx=20)
mi_frame.pack()

btn_clientes = Button(mi_frame, text='Clientes', width=50, height=5, command=registro_clientes)
btn_clientes.grid(row=1, column=0, sticky='e', padx=5, pady=5)

raiz.mainloop()