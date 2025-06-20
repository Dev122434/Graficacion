import sqlite3

conexion = sqlite3.connect("Empresa.db")

# Crear el cursor
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Productos(
               codigo VARCHAR(4) PRIMARY KEY,
               descripcion TEXT,
               precio FLOAT,
               seccion TEXT)
''')

productos = [
    ('5', 'Laptop', 5600, 'tecnologia'),
    ('6', 'Celular', 5000, 'tecnologia'),
    ('7', 'USB', 200.5, 'tecnologia')
]

# Ejecutamos la consulta
cursor.executemany("INSERT INTO Productos VALUES (?, ?, ?, ?)", productos)

conexion.commit()

conexion.close()