import numpy as np

"""
Ejercicio 1: Lista de equipos

Crea una lista con los 5 primeros equipos de la clasificación (puedes inventar el orden).

Muestra en pantalla el primer y último equipo.,

Añade un equipo nuevo al final de la lista.,

Inserta a mano un equipo en la primera posición.,

Elimina un equipo que ya no quieras que esté en la lista.,

"""

# EJERCICIO 1
print("Ejercicio 1:\n")
listaEj1 = ["FNATIC", "T1", "SK04", "Missfist", "ROGUE"]
print("El primero " + listaEj1[0] + " y el utlimo " + listaEj1[-1])
listaEj1.append("GENG")
listaEj1.insert(0, "DRX")
listaEj1.remove("Missfist")

"""
-------------------------------------------------------------------------------------------------------
Ejercicio 2: Jornada de partidos

Crea dos listas:
locales = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]
visitantes = ["Athletic", "Betis", "Cádiz", "Villarreal", "Osasuna"]
imprimir los partidos en formato:
Real Madrid vs Athletic
Barcelona vs Betis

Elimina un partido (por ejemplo, el de Sevilla vs Villarreal).
Añade un nuevo partido con un equipo inventado.

"""

# EJERCICIO 2
print("Ejercicio 2:\n")
locales = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]
visitantes = ["Athletic", "Betis", "Cádiz", "Villarreal", "Osasuna"]

for partidos in range(0, len(locales)):
    print(locales[partidos] + " vs " + visitantes[partidos])

pos = 3
del locales[pos]
del visitantes[pos]

locales.append("Puertollano")
visitantes.append("Ciudad Real")

"""
--------------------------------------------------------------------------------------------
Ejercicio 3: Clasificación de goleadores
Crea una lista con los goles de 6 jugadores:
Muestra cuántos jugadores hay
Ordena la lista de goles de menor a mayor y luego de mayor a menor.
Muestra el máximo y el mínimo de la lista (max() y min()).
Inserta un nuevo jugador con 8 goles en la posición correcta para mantener el orden.
"""

# EJERCICIO 3
print("Ejercicio 3:\n")

jugadores = [2, 3, 4, 1, 6, 0]

print("Hay " + str(len(jugadores)) + " jugadores")

sumatorio = sum(jugadores)

print("Hay " + str(sumatorio) + " goles")
#media = sumatorio / len(jugadores)
media = np.mean(jugadores)
media = round(media, 2)

print("Hay una media de "+ str(media)+ " goles")


jugadores.sort()
print(jugadores)
jugadores.sort(reverse=True)
print(jugadores)

print("El maximo es " + str(max(jugadores)) + " y el minimo es " + str(min(jugadores)))

# jugadores.insert(0,8)


nuevoJugador = 8
aux = 0
for i in range(0, len(jugadores) - 1):
    aux = i
    print(aux)
    if nuevoJugador > jugadores[aux]:
        break

jugadores.insert(aux, nuevoJugador)

print(jugadores)
