from tkinter import *

# Variables globales
operacion = ""
reset_pantalla = False
resultado = 0
memoria = 0

# Funciones
def numero_pulsado(num):
    global reset_pantalla
    if reset_pantalla:
        numero_pantalla.set(num)
        reset_pantalla = False
    else:
        numero_pantalla.set(numero_pantalla.get() + num)

def limpiar():
    global resultado, operacion, reset_pantalla
    numero_pantalla.set("")
    resultado = 0
    operacion = ""
    reset_pantalla = False

def calcular_resultado():
    global resultado, operacion, reset_pantalla
    try:
        num2 = float(numero_pantalla.get())
        if operacion == "suma":
            resultado += num2
        elif operacion == "resta":
            resultado -= num2
        elif operacion == "multiplicacion":
            resultado *= num2
        elif operacion == "division":
            if num2 != 0:
                resultado /= num2
            else:
                numero_pantalla.set("No se puede dividir")
                reset_pantalla = True
                return
        numero_pantalla.set(str(resultado))
        reset_pantalla = True
        operacion = ""
    except:
        numero_pantalla.set("Error")

def suma(num):
    global resultado, operacion, reset_pantalla
    resultado = float(num)
    operacion = "suma"
    reset_pantalla = True

def resta(num):
    global resultado, operacion, reset_pantalla
    resultado = float(num)
    operacion = "resta"
    reset_pantalla = True

def multiplicacion(num):
    global resultado, operacion, reset_pantalla
    resultado = float(num)
    operacion = "multiplicacion"
    reset_pantalla = True

def division(num):
    global resultado, operacion, reset_pantalla
    resultado = float(num)
    operacion = "division"
    reset_pantalla = True

# Funciones de memoria
memoria = 0

def memoria_clear():
    global memoria
    numero_pantalla.set(memoria)
    memoria = 0
    #numero_pantalla.set("")  # Limpia la pantalla también (opcional)

def memoria_recall():
    numero_pantalla.set(str(memoria))  # Muestra el número guardado

def memoria_suma():
    global memoria, reset_pantalla
    try:
        valor = float(numero_pantalla.get())
        memoria += valor
        reset_pantalla = True
    except ValueError:
        numero_pantalla.set("Error")

def memoria_resta():
    global memoria, reset_pantalla
    try:
        valor = float(numero_pantalla.get())
        memoria -= valor
        reset_pantalla = True
    except ValueError:
        numero_pantalla.set("Error")

raiz = Tk()
raiz.title("Calculadora")
raiz.resizable(False, False)

numero_pantalla = StringVar()

pantalla = Entry(raiz, textvariable=numero_pantalla, font=("Arial", 20), bd=10, insertwidth=2, width=18,
                 borderwidth=4, bg="black", fg="#03f943", justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [
    ("MC", memoria_clear), ("MR", memoria_recall), ("M-", memoria_resta), ("M+", memoria_suma),
    ("7", lambda: numero_pulsado("7")), ("8", lambda: numero_pulsado("8")), ("9", lambda: numero_pulsado("9")), ("/", lambda: division(numero_pantalla.get())),
    ("4", lambda: numero_pulsado("4")), ("5", lambda: numero_pulsado("5")), ("6", lambda: numero_pulsado("6")), ("x", lambda: multiplicacion(numero_pantalla.get())),
    ("1", lambda: numero_pulsado("1")), ("2", lambda: numero_pulsado("2")), ("3", lambda: numero_pulsado("3")), ("-", lambda: resta(numero_pantalla.get())),
    ("0", lambda: numero_pulsado("0")), (".", lambda: numero_pulsado(".")), ("=", calcular_resultado), ("+", lambda: suma(numero_pantalla.get())),
    ("AC", limpiar)
]

fila = 1
col = 0
for texto, comando in botones:
    Button(raiz, text=texto, width=6, height=2, font=("Arial", 12), command=comando).grid(row=fila, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        fila += 1

raiz.mainloop()
