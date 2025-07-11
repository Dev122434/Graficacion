import sqlite3

conexion = sqlite3.connect("Prueba.db")

# Crear el cursor
cursor = conexion.cursor()

cursor.execute('''SELECT SUM(CASE WHEN Genero = "Femenino" THEN 1 ELSE 0 END)
                AS Femenino,
                SUM(CASE WHEN Genero = "Masculino" THEN 1 ELSE 0 END)
                AS Masculino
            FROM Clientes
''')

# Obtenemos los registros
total = cursor.fetchone()

# Guardamos los cambios en la BD
conexion.commit()

# Cerramos la conexion de la BD
conexion.close()
