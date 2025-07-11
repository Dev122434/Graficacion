import matplotlib.pyplot as plt

# Datos de la grafica
x1 = [1, 2, 3, 4, 5]
y1 = [6, 7, 8, 9, 10]
x2 = [12, 13, 14, 15, 16]
y2 = [17, 18, 19, 20, 21]

plt.bar(x1, y1, color='purple', width=0.5, label='Ventas 1')
plt.bar(x2, y2, color='red', width=0.5, label='Ventas 2')

# Metodo para agregar un titulo a la grafica
plt.title('Programa 04')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()