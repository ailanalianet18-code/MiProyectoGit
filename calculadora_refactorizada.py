
"""Calculadora refactorizada aplicando SRP y OCP."""


def mostrar_menu():
    """Muestra las opciones disponibles de la calculadora."""
    print("\nCALCULADORA")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def leer_numero(mensaje):
    """Solicita un número al usuario y lo devuelve."""
    return float(input(mensaje))


def sumar(numero1, numero2):
    """Devuelve la suma de dos números."""
    return numero1 + numero2


def restar(numero1, numero2):
    """Devuelve la resta de dos números."""
    return numero1 - numero2


def multiplicar(numero1, numero2):
    """Devuelve el producto de dos números."""
    return numero1 * numero2


def dividir(numero1, numero2):
    """Divide dos números y controla la división entre cero."""
    if numero2 == 0:
        return "Error: No se puede dividir entre cero."
    return numero1 / numero2


def calcular(opcion, numero1, numero2):
    """Ejecuta la operación seleccionada."""
    if opcion not in operaciones:
        return "Opción incorrecta."
    return operaciones[opcion](numero1, numero2)


def ejecutar_calculadora():
    """Controla el funcionamiento principal de la calculadora."""
    while True:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))

        if opcion == 5:
            print("Finalizada.")
            break

        if opcion not in operaciones:
            print("Opción incorrecta.")
            continue

        numero1 = leer_numero("Ingrese el primer número: ")
        numero2 = leer_numero("Ingrese el segundo número: ")

        resultado = calcular(opcion, numero1, numero2)
        print("Resultado:", resultado)


# Diccionario que permite organizar las operaciones.
operaciones = {
    1: sumar,
    2: restar,
    3: multiplicar,
    4: dividir
}


if __name__ == "__main__":
    ejecutar_calculadora()
