import matplotlib.pyplot as plt

# Datos de la grafica
x1 = [1, 2, 3, 4, 5]
y1 = [50, 60, 70, 80]
x2 = [1, 2, 3]
y2 = [5, 6, 7]

plt.bar(x1, y1, color='purple', width=0.5, label='Ventas 1')
plt.bar(x2, y2, color='red', width=0.5, label='Ventas 2')

# Metodo para agregar un titulo a la grafica
plt.title('Programa 02')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()