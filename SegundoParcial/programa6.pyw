import sqlite3

conexion = sqlite3.connect("Empresa.db")

# Crear el cursor
cursor = conexion.cursor()

cursor.execute("INSERT INTO Productos VALUES('4', 'Cargador', 10.5, 'tecnologia')")

conexion.commit()

conexion.close()