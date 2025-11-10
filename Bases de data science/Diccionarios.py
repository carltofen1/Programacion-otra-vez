# Ejercicio 1: crear un diccionario a partir de dos listas
# Tengo una lista de nombres y otra de edades, las uno para formar un diccionario
nombres = ['Ana', 'Luis', 'Marta', 'Pedro']
edades = [21, 30, 25, 29]
personas = {n: e for n, e in zip(nombres, edades)}
print(personas)

# Resultado: {'Ana': 21, 'Luis': 30, 'Marta': 25, 'Pedro': 29}
# Básicamente cada nombre se empareja con su edad, uno a uno.
print('-' * 40)

# Ejercicio 2: filtrar valores dentro del diccionario
# Quiero quedarme solo con las personas mayores de 25 años
mayores = {n: e for n, e in personas.items() if e > 25}
print(mayores)

# Resultado: {'Luis': 30, 'Pedro': 29}
# .items() permite recorrer clave y valor al mismo tiempo.
print('-' * 40)

# Ejercicio 3: contar cuántas veces se repite cada palabra
# Tengo una lista de palabras y quiero saber cuántas veces aparece cada una
palabras = ['perro', 'gato', 'gato', 'pez', 'perro', 'perro']
conteo = {p: palabras.count(p) for p in set(palabras)}
print(conteo)

# Resultado: {'perro': 3, 'gato': 2, 'pez': 1}
# Uso set() para quitar duplicados y count() para contar cada palabra.
print('-' * 40)

# Ejercicio 4: convertir datos anidados
# Tengo un diccionario con estudiantes y sus notas, quiero calcular el promedio
notas = {
    'Camila': [14, 16, 15],
    'Sofía': [18, 17, 19],
    'Carlos': [11, 14, 13]
}
promedios = {n: round(sum(v) / len(v), 1) for n, v in notas.items()}
print(promedios)

# Resultado: {'Camila': 15.0, 'Sofía': 18.0, 'Carlos': 12.7}
# Uso round() para redondear y hago el promedio directo.
print('-' * 40)

# Ejercicio 5: cambiar claves y valores
# A veces quiero invertir el diccionario, que el valor sea la clave y al revés
ciudades = {'Lima': 'Perú', 'Bogotá': 'Colombia', 'Quito': 'Ecuador'}
invertido = {v: k for k, v in ciudades.items()}
print(invertido)

# Resultado: {'Perú': 'Lima', 'Colombia': 'Bogotá', 'Ecuador': 'Quito'}
# Simple intercambio clave↔valor.
print('-' * 40)

# Ejercicio 6: usar dict() para crear desde tuplas
# Tengo una lista de tuplas (producto, precio) y la convierto a diccionario
productos = [('pan', 2.5), ('leche', 3.8), ('huevo', 5.2)]
precios = dict(productos)
print(precios)

# Resultado: {'pan': 2.5, 'leche': 3.8, 'huevo': 5.2}
# dict() entiende directo una lista de tuplas (clave, valor).
print('-' * 40)

# Ejercicio 7: sumar valores por categoría
# Supón que tengo ventas agrupadas por tipo, quiero sumar lo vendido de cada tipo
ventas = [('pan', 10), ('leche', 20), ('pan', 15), ('leche', 5), ('huevo', 12)]
resumen = {}
for prod, cant in ventas:
    resumen[prod] = resumen.get(prod, 0) + cant
print(resumen)

# Resultado: {'pan': 25, 'leche': 25, 'huevo': 12}
# .get() sirve para asignar un valor inicial (0 si no existe).
print('-' * 40)

# Ejercicio 8: agrupar valores en listas
# En lugar de sumar, quiero juntar los valores de cada producto en listas
grupos = {}
for prod, cant in ventas:
    grupos.setdefault(prod, []).append(cant)
print(grupos)

# Resultado: {'pan': [10, 15], 'leche': [20, 5], 'huevo': [12]}
# setdefault() crea la lista vacía si no existe aún.
print('-' * 40)

# Ejercicio 9: combinar varios diccionarios
# Tengo tres diccionarios de precios en distintas tiendas
a = {'pan': 2.5, 'leche': 3.5}
b = {'huevo': 4.0, 'pan': 2.8}
c = {'queso': 8.0}
unido = a | b | c
print(unido)

# Resultado: {'pan': 2.8, 'leche': 3.5, 'huevo': 4.0, 'queso': 8.0}
# El operador | une diccionarios y si hay claves repetidas, se queda el último.
print('-' * 40)

# Ejercicio 10: crear un diccionario con condiciones y operaciones
# Quiero convertir precios a dólares, pero solo los mayores de 3 soles
cambio = {p: round(v / 3.7, 2) for p, v in unido.items() if v > 3}
print(cambio)

# Resultado: {'leche': 0.95, 'huevo': 1.08, 'queso': 2.16}
# Pequeño filtrado + operación matemática dentro del dict comprehension.
