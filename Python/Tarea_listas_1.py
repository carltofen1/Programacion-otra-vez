# Creación del menú
lista = []
# Nota: la lista está fuera del bucle porque, si estuviera dentro del while,
# se reiniciaría cada vez que el usuario elija una opción.

while True:
    print("""
Bienvenido al menú
Por favor selecciona una de las opciones

Opción 1: Agregar datos a una lista
Opción 2: Verificar cuántos elementos hay en la lista
Opción 3: Mostrar de qué tipo es cada valor en la lista
Opción 4: Agregar palabras, compararlas y mostrar la más larga
Opción 5: Sumar los valores numéricos en la lista
Opción 6: Reiniciar la lista (crear una nueva lista vacía)
Opción 7: Salir del menú
Opción extra: Diferencias entre una tupla y una lista
      """)

    opcion = input("Elige una opción (1-7 o 'extra'): ")

    # Opción 1: Agregar datos
    if opcion == "1":
        numeros = int(input("¿Cuántos datos quieres agregar?: "))
        for i in range(numeros):
            tipo = input("¿Qué tipo de elemento deseas ingresar? (entero, decimal o texto): ")
            if tipo.lower() == "entero":
                digito = int(input("Ingresa el elemento: "))
            elif tipo.lower() == "decimal":
                digito = float(input("Ingresa el elemento: "))
            else:
                digito = input("Ingresa el elemento: ")
            lista.append(digito)
            print("Elemento agregado.")

    # Opción 2: Cantidad de elementos
    elif opcion == "2":
        print("La lista contiene", len(lista), "elementos.")

    # Opción 3: Tipos de valores
    elif opcion == "3":
        for elemento in lista:
            if isinstance(elemento, int):
                print(f"El elemento {elemento} es un número entero.")
            elif isinstance(elemento, float):
                print(f"El elemento {elemento} es un número decimal.")
            elif isinstance(elemento, str):
                print(f"El elemento '{elemento}' es un texto.")
            else:
                print(f"El elemento {elemento} es de tipo {type(elemento)}")

    # Opción 4: Palabra más larga
    elif opcion == "4":
        palabras = [str(e) for e in lista if isinstance(e, str)]
        if palabras:
            palabra_larga = max(palabras, key=len)
            print(f"La palabra más larga es '{palabra_larga}' con {len(palabra_larga)} letras.")
        else:
            print("No hay palabras en la lista.")

    # Opción 5: Sumar valores numéricos
    elif opcion == "5":
        numeros = [e for e in lista if isinstance(e, (int, float))]
        if numeros:
            print("La suma de los valores numéricos es:", sum(numeros))
        else:
            print("No hay valores numéricos en la lista.")

    # Opción 6: Reiniciar lista
    elif opcion == "6":
        lista = []
        print("La lista ha sido reiniciada.")

    # Opción 7: Salir
    elif opcion == "7":
        print("Saliendo del programa...")
        break

    # Opción extra: Diferencias entre lista y tupla
    elif opcion.lower() == "extra":
        print("""
Lista:
- Se escribe con corchetes [].
- Es mutable (puede cambiarse: agregar, eliminar o modificar elementos).
- Ejemplo: [1, 2, "hola"]

Tupla:
- Se escribe con paréntesis ().
- Es inmutable (no se puede modificar después de creada).
- Ejemplo: (1, 2, "hola")
        """)

    else:
        print("Opción inválida, intenta nuevamente.")
