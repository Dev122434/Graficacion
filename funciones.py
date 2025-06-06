from tkinter import StringVar
operacion = ""
reset_pantalla = False
resultado = 0

numero_pantalla = StringVar()
def numero_pulsado(num):
    global operacion
    global reset_pantalla

    if reset_pantalla != False:
        numero_pantalla.set(num)
        reset_pantalla = False
    else:
        numero_pantalla.set(numero_pantalla.get() + num)

num1 = 0
contador_resta = 0

def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if (contador_resta == 0):
        num1 = float(num)
        resultado = num1
    else:
        resultado = float(resultado) - float(num)
        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()

    contador_resta += 1
    operacion = "resta"
    reset_pantalla = True

contador_suma = 0

def suma(num):
    global operacion
    global resultado
    global num1
    global contador_suma
    global reset_pantalla

    if (contador_suma == 0):
        num1 = float(num)
        resultado = num1
    else:
        resultado = float(resultado) + float(num)
        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()

    contador_suma += 1
    operacion = "suma"
    reset_pantalla = True

contador_mult = 0

def multiplicacion(num):
    global operacion
    global resultado
    global num1
    global contador_mult
    global reset_pantalla

    if (contador_mult == 0):
        num1 = float(num)
        resultado = num1
    else:
        resultado = float(resultado) * float(num)
        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()

    contador_mult += 1
    operacion = "multiplicacion"
    reset_pantalla = True

contador_div = 0

def division(num):
    global operacion
    global resultado
    global num1
    global contador_div
    global reset_pantalla

    if (contador_div == 0):
        num1 = float(num)
        resultado = num1
    else:
        if (float(num) != 0):
            resultado = float(resultado) / float    (num)
            numero_pantalla.set(resultado)
            resultado = numero_pantalla.get()
        else:
            numero_pantalla.set("No se puede dividir")
            resultado = numero_pantalla.get()

    contador_div += 1
    operacion = "division"
    reset_pantalla = True