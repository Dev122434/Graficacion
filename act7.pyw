def codigo_boton() -> None:
    miNombre.set("Lenguaje Python")
    miPass.set("Python")
    mi
from tkinter import *

raiz = Tk()

raiz.geometry("450x400")
miFrame = Frame(width=1200, height=600)
miFrame.pack()
miNombre = StringVar()
miPass = StringVar()
miApellido = StringVar()
miDireccion = StringVar()

lblNombre = Label(miFrame, text="Nombre: ")
lblNombre.grid(row=0, column=0, sticky='e', padx=10, pady=10)
lblPass = Label(miFrame, text="Password")
lblPass.grid(row=1, column=0, sticky='e', padx=10, pady=10)
lblApellido = Label(miFrame, text="Apellido")
lblApellido.grid(row=2, column=0, sticky='e', padx=10, pady=10)
lblDireccion = Label(miFrame, text="Direccion")
lblDireccion.grid(row=3, column=0, sticky='e', padx=10, pady=10)


txtNombre = Entry(miFrame, textvariable=miNombre)
txtNombre.grid(row=0, column=1, sticky='e', padx=10, pady=10)
txtNombre.config(fg='red', font=('Comic Sans MS', 18), justify="center")
txtPass = Entry(miFrame, textvariable=miPass, show='*')
txtPass.grid(row=1, column=1, sticky='e', padx=10, pady=10)
txtPass.config(fg='blue', font=('Comic Sans MS', 18), justify="right")
txtApellido = Entry(miFrame)
txtApellido.grid(row=2, column=1, sticky='e', padx=10, pady=10)
txtApellido.config(fg='blue', font=('Comic Sans MS', 18), justify="right")
txtDireccion = Entry(miFrame)
txtDireccion.grid(row=3, column=1, sticky='e', padx=10, pady=10)
txtDireccion.config(fg='blue', font=('Comic Sans MS', 18), justify="right")
btnEnvio = Button(raiz, text='Enviar', command=codigo_boton)
btnEnvio.pack()

lblComentario = Label(miFrame, text="Comentarios")
lblComentario.grid(row=4, column=0, sticky='e', padx=10, pady=10)
textoComentario = Text(miFrame, width=26, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)
scrollVer = Scrollbar(miFrame, command=textoComentario.yview)
scrollVer.grid(row=4, column=2, sticky='nsew')
textoComentario.config(yscrollcommand=scrollVer.set)
raiz.mainloop()
