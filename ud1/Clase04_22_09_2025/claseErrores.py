def ingresarUnNumero():
    try:
        numero = int(input("Ingresa un numero: "))
        return numero
    except ValueError as error:
        print(f"Has dado un error de tipo valor, no has ingresado un número entero {type(error)}")
    except Exception as error:
        print(f"Has dado un error de : {type(error)}")


try:
    numero = ingresarUnNumero()
    numero *=3

    #resultado= 10/0
    #matriz= [1,2,3]
    #resultado1 = 8-10
    #if resultado1 <0:
    #    raise Exception('Hola')
    #print(matriz[3])


except IndexError as erro:
    print(f"Se ha dado un error de rango: {erro}")
except ZeroDivisionError as erro:
    print(f"Se ha dado un error de  division de 0: {erro}")
except Exception as e:
    print(f"Has dado un fallo: {type(e)}")
finally:
    print("finalizando")




