from tkinter import *
from funciones import *

raiz = Tk()
raiz.geometry("400x100")
mi_frame = Frame(raiz)
raiz.title("Calculadora Basica")
mi_frame.pack()

operacion = ""
reset_pantalla = False
resultado = 0

numero_pantalla = StringVar()

pantalla = Entry(mi_frame, textvariable=numero_pantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

boton1 = Button(mi_frame, text="1", width=3, command=lambda:numero_pulsado("1"))
boton1.grid(row=5, column=1)
boton2 = Button(mi_frame, text="2", width=3, command=lambda:numero_pulsado("2"))
boton2.grid(row=5, column=2)
boton3 = Button(mi_frame, text="3", width=3, command=lambda:numero_pulsado("3"))
boton3.grid(row=5, column=3)
boton4 = Button(mi_frame, text="4", width=3, command=lambda:numero_pulsado("4"))
boton4.grid(row=6, column=1)
boton5 = Button(mi_frame, text="5", width=3, command=lambda:numero_pulsado("5"))
boton5.grid(row=6, column=2)
boton6 = Button(mi_frame, text="6", width=3, command=lambda:numero_pulsado("6"))
boton6.grid(row=6, column=3)
boton7 = Button(mi_frame, text="7", width=3, command=lambda:numero_pulsado("7"))
boton7.grid(row=7, column=1)
boton8 = Button(mi_frame, text="8", width=3, command=lambda:numero_pulsado("8"))
boton8.grid(row=7, column=2)
boton9 = Button(mi_frame, text="9", width=3, command=lambda:numero_pulsado("9"))
boton9.grid(row=7, column=3)

boton0 = Button(mi_frame, text="0", width=3, command=lambda:numero_pulsado("0"))
boton0.grid(row=8, column=1)

boton_rest = Button(mi_frame, text="-", width=3, command=lambda:resta(numero_pantalla.get()))
boton_rest.grid(row=5, column=4)
boton_sum = Button(mi_frame, text="+", width=3, command=lambda:suma(numero_pantalla.get()))
boton_sum.grid(row=5, column=5)

boton_mult = Button(mi_frame, text="*", width=3, command=lambda:multiplicacion(numero_pantalla.get()))
boton_mult.grid(row=6, column=4)

boton_div = Button(mi_frame, text="/", width=3, command=lambda:division(numero_pantalla.get()))
boton_div.grid(row=6, column=5)

raiz.mainloop()