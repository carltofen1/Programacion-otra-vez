"""
from matplotlib import pyplot as plt

estudiantes = ["Juan", "María", "José"]
notas = [9, 8.5, 6.5]

plt.bar(x=estudiantes,height=notas)
plt.show()

"""

from random import choice

estudiantes_2 = ["Juan", "María", "José", "Érica"]

estudiante = choice(estudiantes_2)

print(estudiante)