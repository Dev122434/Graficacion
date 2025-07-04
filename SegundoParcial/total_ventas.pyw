import sqlite3

inicio = '2024-04-16'
fin = '2025-04-16'

conexion = sqlite3.connect("Prueba.db")

# Crear el cursor
cursor = conexion.cursor()

cursor.execute('''SELECT Fecha, SUM(Total)
               FROM Ventas WHERE Fecha
               BETWEEN ? AND ? GROUP BY Fecha
               ORDER BY Fecha
''', (inicio, fin))

# Obtenemos los registros
datos = cursor.fetchall()

# Guardamos los cambios en la BD
conexion.commit()

# Cerramos la conexion de la BD
conexion.close()

# Imprimimos los registros
print(datos)