# Filtrar y elevar al cuadrado solo los números pares de una lista
pares_cuadrados = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))
print(pares_cuadrados)

# Ordenar una lista de tuplas por edad
personas = [('Ana', 23), ('Luis', 31), ('María', 19)]
orden_edad = sorted(personas, key=lambda x: x[1])
print(orden_edad)

# Calcular raíces cuadradas con lambda y map
nums3 = [4, 9, 16, 25]
raices = list(map(lambda x: x**0.5, nums3))
print(raices)

# Filtrar palabras que contengan la letra "a"
palabras = ['python', 'data', 'lambda', 'github', 'analytics']
palabras_con_a = list(filter(lambda x: 'a' in x, palabras))
print(palabras_con_a)

# Ordenar palabras según su longitud
ordenadas = sorted(palabras, key=lambda x: len(x))
print(ordenadas)

# Convertir una lista de palabras a mayúsculas
mayus = list(map(lambda x: x.upper(), palabras))
print(mayus)

# Comparar dos números con una expresión condicional dentro del lambda
comparar = lambda a, b: 'mayor' if a > b else 'menor' if a < b else 'igual'
print(comparar(5, 5))

# Promedio de una lista con lambda
nums = [2, 5, 8, 10, 3, 7]
promedio = lambda lista: sum(lista) / len(lista)
print(promedio(nums))

# Invertir una palabra
reversa = lambda s: s[::-1]
print(reversa('Patrick'))

# Multiplicar tres valores
multiplica = lambda a, b, c: a * b * c
print(multiplica(2, 3, 4))