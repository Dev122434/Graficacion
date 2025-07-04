import matplotlib.pyplot as plt

# Datos de la grafica
x1 = [1, 2, 3, 4, 5]
y1 = [11, 12, 13, 14]
x2 = [1, 2, 3]
y2 = [5, 6, 7]

# Metodo para agregar un titulo a la grafica
plt.title('Programa 02')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
# Configurar las caracteriticas de la grafica
plt.plot(x1, y1, color='blue', linewidth=3, label='Ventas')
#plt.plot(x2, y2, color='blue', linewidth=3, label='Ventas')

# Mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()