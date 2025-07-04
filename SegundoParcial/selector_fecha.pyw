from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

def mostrar_fecha() -> None:
    fecha = selectorFecha.get()
    print(fecha)

raiz = Tk()
raiz.title('Selector de Fecha')
raiz.geometry("300x180")

lblFecha = Label(raiz, text='Selecciona una fecha: ', font=('Arial', 12)).pack(pady=10)

selectorFecha = DateEntry(raiz, width=16, background='navy', foreground='white',
                          borderwidth=2, date_pattern='yyyy-mm-dd')
selectorFecha.pack(pady=10)

btnMostrarFecha = Button(raiz, text='Mostrar fecha',
command=mostrar_fecha).pack(pady=10)

raiz.mainloop()