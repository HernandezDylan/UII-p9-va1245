# Programa realizado por Hernandez Dylan NC=1245
# Grafica de pastel (Pie) con Matplotlib

import matplotlib.pyplot as plt

# Materias
materias = ['Matematicas', 'Programacion', 'Ingles', 'Vision Artificial', 'Machine Learning']

# Calificaciones de cada materia
calificaciones = [90, 85, 95, 88, 92]

# Crear grafica de pastel
plt.pie(calificaciones, labels=materias, autopct='%1.1f%%')

# Titulo y etiquetas
plt.title('NC 1245 - Calificaciones')

plt.xlabel('Materias')
plt.ylabel('Calificaciones')

# Guardar imagen
plt.savefig('pastel_1245.png')

# Mostrar grafica
plt.show()

# Imprimir datos del alumno
print("Programa realizado por: Hernadez Dylan NC=1245")
