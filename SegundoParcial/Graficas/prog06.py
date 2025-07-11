import matplotlib.pyplot as plt

# Datos de la grafica
x1 = [19, 20, 11, 12, 11]
y1 = [14, 34, 40, 50, 13]
x2 = [23.1, 45.5, 34.5, 24, 21]
y2 = [12, 34, 45, 23, 43]

plt.scatter(x1, y1, label='Datos 1', color='red')
plt.scatter(x2, y2, label='Datos 2', color='blue')

# Metodo para agregar un titulo a la grafica
plt.title('Programa 06')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar la figura
plt.legend()
plt.grid()
plt.show()