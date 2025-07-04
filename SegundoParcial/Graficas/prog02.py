import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]
b = [50, 60, 70, 80]

# Metodo para agregar un titulo a la grafica
plt.title('Programa 02')
plt.plot(a, b, color='blue', linewidth=3, label='linea')
plt.legend()
plt.show()