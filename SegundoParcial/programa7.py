import sqlite3

conexion = sqlite3.connect("Empresa.db")

# Crear el cursor
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Proveedores(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT,
               credito FLOAT,
               celular INTEGER
               )
''')

proveedores = [
    ('Marcos', 10000.0, 14242424),
    ('Jose', 20000.0, 2453535),
    ('Julio', 30000.0, 243546)
]

cursor.executemany("INSERT INTO Proveedores VALUES(NULL, ?, ?, ?)", proveedores)

cursor.execute('SELECT * FROM Proveedores WHERE id = (SELECT MAX(id) FROM Proveedores)')

lista_proveedores = cursor.fetchall()

print(lista_proveedores[0][0])

conexion.commit()

conexion.close()