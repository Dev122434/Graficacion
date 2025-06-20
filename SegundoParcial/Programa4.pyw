import sqlite3

conexion = sqlite3.connect("Empresa.db")

# Crear el cursor
cursor = conexion.cursor()

cursor.execute('SELECT * FROM Clientes')

clientes = cursor.fetchall()

print(f'\nTodos los clientes\n{clientes}')

print('\nLos Clientes son: ')
for item in clientes:
    print(item)

print('Codigo:\t\tNombre\t\t\tCorreo')
print('------------------------------------------')
for item in clientes:
    print(f'{item[0]:5}\t {item[1]:15}\t {item[4]:15}')

conexion.commit()

conexion.close()