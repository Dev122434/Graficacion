import sqlite3

conexion = sqlite3.connect("Empresa.db")

# Crear el cursor
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER,
                Nombre TEXT NOT NULL,
                Domicilio VARCHAR(40),
                Celular INTEGER,
                Correo TEXT
)
''')

# Verificar que se va a realizar un cambio en la Tabla y confirmar los cambios
conexion.commit()

# Cerrar la base de datos
conexion.close()
