import sqlite3

conexion = sqlite3.connect("Empresa.db")

# Crear el cursor
cursor = conexion.cursor()

# Creacion de una lista para insertar varios registros en la bd
clientes = [
    (4, 'Jose', 'UDL', '2423543', 'josecorreo@gmail.com'),
    (5, 'Maria', 'UDL', '2425435', 'mariacorreo@gmail.com'),
    (6, 'Julia', 'UDL', '2452424', 'juliacorreo@gmail.com')
]

# Ejecutamos la consulta
cursor.executemany("INSERT INTO Clientes VALUES (?, ?, ?, ?, ?)", clientes)

conexion.commit()

conexion.close()