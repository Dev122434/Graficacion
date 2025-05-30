from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=600, height=500)
miFrame.pack()
lblNombre = Label(miFrame, text='Nombre')
lblNombre.place(x=100, y=100)

txtNombre = Entry(miFrame)
txtNombre.place(x=180, y=100)

raiz.mainloop()