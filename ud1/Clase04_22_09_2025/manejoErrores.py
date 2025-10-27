def divisionZero():
    try:
        resultado = 10 / 0
    except ZeroDivisionError:

        print("No se puede dividir entre cero.")

def multiple():
    try:
        numero = int(input("Introduce un número: "))
        resultado = 10 / numero
    except ValueError:
        print("Debes introducir un número válido.")
    except ZeroDivisionError:

        print("No se puede dividir entre cero.")


def cualquiera():
    try:
        resultado = 10 / int(input("Introduce un número: "))
    except:
        print("Algo salió mal.")


def conElse():
    try:
        resultado = 10 / int(input("Introduce un número: "))
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    except ValueError:
        print("Debes introducir un número válido.")
    else:
        print(f"El resultado es: {resultado}")


def conFinally():
    try:
        archivo = open("archivo.txt", "r")
        contenido = archivo.read()
    except FileNotFoundError:
        print("El archivo no se encontró.")
    finally:
        archivo.close()

def verificar_numero(numero):
    if numero < 0:
        raise ValueError("El número no puede ser negativo.")
    return numero

def lanzarExcepciones():
    try:
        verificar_numero(-5)
    except ValueError as e:
        print(f"Error: {e}")



#divisionZero()
#multiple()
#cualquiera()
#conElse()
#conFinally()
#verificar_numero(-1)
#lanzarExcepciones()