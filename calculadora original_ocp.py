opcion = 0

while opcion != 5:

    print("\n CALCULADORA ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion >= 1 and opcion <= 4:

        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            print("Resultado:", numero1 + numero2)

        elif opcion == 2:
            print("Resultado:", numero1 - numero2)

        elif opcion == 3:
            print("Resultado:", numero1 * numero2)

        elif opcion == 4:
            if numero2 != 0:
                print("Resultado:", numero1 / numero2)
            else:
                print("Error: No se puede dividir entre cero.")

    elif opcion == 5:
        print("finalizada.")

    else:
        print("Opción incorrecta.")