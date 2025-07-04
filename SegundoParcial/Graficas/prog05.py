import matplotlib.pyplot as plt

# Datos de la grafica
a = [19, 20, 11, 12, 11, 50, 60, 70, 80,22, 34, 54, 53, 9]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(a, bins, histtype='bar', rwidth=0.8, color='red')

# Metodo para agregar un titulo a la grafica
plt.title('Programa 05')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar la figura
plt.grid()
plt.show()