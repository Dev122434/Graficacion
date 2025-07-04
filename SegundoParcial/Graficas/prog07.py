import matplotlib.pyplot as plt

# Datos de la grafica
divisiones = [5, 1, 3, 4]
colores = ['red', 'purple', 'orange', 'blue']
actividades = ['Programacion', 'Base De Datos', 'IA', 'Ingles']

# Configurar las caracteristicas del grafico
plt.pie(divisiones, colors=colores, labels=actividades, startangle=90,
        shadow=True, explode=(0, 0, 0, 0.1), autopct='%1.1f%%')

# Metodo para agregar un titulo a la grafica
plt.title('Programa 07')

# Mostrar la figura
plt.show()