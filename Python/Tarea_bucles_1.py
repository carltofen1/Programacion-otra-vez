def menu_interactivo():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Cuenta regresiva de un número en 3 en 3")
        print("2. Multiplicación de varios números")
        print("3. Verificar si una palabra es palíndroma")
        print("4. Encontrar la palabra más larga")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        # Opción 1: Cuenta regresiva
        if opcion == "1":
            numero = int(input("Dame un número múltiplo de 3: "))
            while numero % 3 != 0:
                print("El número debe ser múltiplo de 3")
                numero = int(input("Dame un número múltiplo de 3: "))
            for i in range(numero, -1, -3):
                print(i)

        # Opción 2: Multiplicación
        elif opcion == "2":
            cantidad = int(input("¿Cuántos números quieres multiplicar?: "))
            resultado = 1
            for i in range(cantidad):
                num = float(input(f"Ingrese el número {i+1}: "))
                resultado *= num
            print("El resultado de la multiplicación es:", resultado)

        # Opción 3: Palíndromo
        elif opcion == "3":
            palabra = input("Ingrese la palabra: ")
            if palabra == palabra[::-1]:
                print("La palabra es palíndroma")
            else:
                print("La palabra no es palíndroma")

        # Opción 4: Palabra más larga
        elif opcion == "4":
            lista = []
            cantidad = int(input("¿Cuántas palabras quieres comparar?: "))
            for i in range(cantidad):
                palabra = input(f"Ingrese la palabra {i+1}: ")
                lista.append(palabra)

            palabra_larga = max(lista, key=len)
            print(f"La palabra más larga es '{palabra_larga}' con {len(palabra_larga)} letras.")

        # Opción 5: Salir
        elif opcion == "5":
            salir = input("¿Deseas salir del programa? (SI/NO): ").upper()
            if salir == "SI":
                print("Saliendo del programa...")
                break

        else:
            print("Opción inválida, intenta de nuevo.")
