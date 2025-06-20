from tkinter import *

raiz = Tk()

raiz.geometry("450x400")
miFrame = Frame(width=1200, height=600)
miFrame.pack()
miNombre = StringVar()
miPass = StringVar()

lblNombre = Label(miFrame, text="Nombre: ")
lblNombre.grid(row=0, column=0, sticky='e', padx=10, pady=10)
lblPass = Label(miFrame, text="Password")
lblPass.grid(row=1, column=0, sticky='e', padx=10, pady=10)

txtNombre = Entry(miFrame, textvariable=miNombre)
txtNombre.grid(row=0, column=1, sticky='e', padx=10, pady=10)
txtNombre.config(fg='red', font=('Comic Sans MS', 18), justify="center")
txtPass = Entry(miFrame, textvariable=miPass, show='*')
txtPass.grid(row=1, column=1, sticky='e', padx=10, pady=10)
txtPass.config(fg='blue', font=('Comic Sans MS', 18), justify="center")

raiz.mainloop()
