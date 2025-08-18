import random

# Opciones válidas
opciones = ["piedra", "papel", "tijera"]

# Función para determinar el ganador
def determinar_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        return "Jugador 1"
    else:
        return "Jugador 2"

# Función para mostrar reglas
def mostrar_reglas():
    print("\n--- Reglas del juego ---")
    print("1. Piedra gana a tijera")
    print("2. Tijera gana a papel")
    print("3. Papel gana a piedra")
    print("Puedes jugar en distintos modos: 1 jugador, contra la computadora o multijugador.")
    print("¡Diviértete!\n")

# Función para mostrar estadísticas
def mostrar_estadisticas(estadisticas, resumen, partidas_jugadas):
    if partidas_jugadas == 0:
        print("\nNo hay estadísticas recientes.\n")
    else:
        print("\n--- Resumen ---")
        print(f"Número de partidas realizadas: {partidas_jugadas}")
        for i, partida in enumerate(resumen, start=1):
            print(f"Partida {i}: {partida}")
        print("\n--- Estadísticas ---")
        for jugador, datos in estadisticas.items():
            print(f"{jugador}: {datos['ganadas']} ganadas, {datos['perdidas']} perdidas, {datos['empates']} empates")
        print("")

# Función para actualizar estadísticas
def actualizar_estadisticas(nombre1, nombre2, resultado, estadisticas, resumen):
    if nombre1 not in estadisticas:
        estadisticas[nombre1] = {"ganadas": 0, "perdidas": 0, "empates": 0}
    if nombre2 not in estadisticas:
        estadisticas[nombre2] = {"ganadas": 0, "perdidas": 0, "empates": 0}

    if resultado == "Empate":
        estadisticas[nombre1]["empates"] += 1
        estadisticas[nombre2]["empates"] += 1
        resumen.append(f"{nombre1} empató - {nombre2} empató")
    elif resultado == "Jugador 1":
        estadisticas[nombre1]["ganadas"] += 1
        estadisticas[nombre2]["perdidas"] += 1
        resumen.append(f"{nombre1} ganó - {nombre2} perdió")
    else:
        estadisticas[nombre2]["ganadas"] += 1
        estadisticas[nombre1]["perdidas"] += 1
        resumen.append(f"{nombre1} perdió - {nombre2} ganó")

    return estadisticas, resumen

# Función para jugar una partida
def partida(nombre1, nombre2, modo, estadisticas, resumen):
    if modo == "1":  # Contra computadora
        jug1 = input(f"{nombre1}, elige piedra, papel o tijera: ").lower()
        while jug1 not in opciones:
            jug1 = input("Opción inválida. Intenta de nuevo: ").lower()
        jug2 = random.choice(opciones)
        print(f"{nombre2} eligió: {jug2}")
    else:  # Multijugador
        jug1 = input(f"{nombre1}, elige piedra, papel o tijera: ").lower()
        while jug1 not in opciones:
            jug1 = input("Opción inválida. Intenta de nuevo: ").lower()
        print("\n" * 30)  # ocultar elección
        jug2 = input(f"{nombre2}, elige piedra, papel o tijera: ").lower()
        while jug2 not in opciones:
            jug2 = input("Opción inválida. Intenta de nuevo: ").lower()

    resultado = determinar_ganador(jug1, jug2)
    if resultado == "Empate":
        print("¡Empate!")
    elif resultado == "Jugador 1":
        print(f"¡Ganó {nombre1}!")
    else:
        print(f"¡Ganó {nombre2}!")

    return actualizar_estadisticas(nombre1, nombre2, resultado, estadisticas, resumen)

# Función para jugar en cualquier modo
def jugar(modo):
    estadisticas = {}
    resumen = []
    partidas_jugadas = 0

    if modo == "1":
        nombre1 = input("Ingrese el nombre del jugador: ")
        nombre2 = "Computadora"
    elif modo == "2":
        nombre1 = input("Ingrese el nombre del Jugador 1: ")
        nombre2 = input("Ingrese el nombre del Jugador 2: ")
    else:
        print("Modo inválido")
        return

    definir = input("¿Desea definir un número de partidas? (s/n): ").lower()
    if definir == "s":
        n = int(input("Ingrese el número de partidas: "))
        for _ in range(n):
            partidas_jugadas += 1
            estadisticas, resumen = partida(nombre1, nombre2, modo, estadisticas, resumen)
    else:
        seguir = "s"
        while seguir == "s":
            partidas_jugadas += 1
            estadisticas, resumen = partida(nombre1, nombre2, modo, estadisticas, resumen)
            seguir = input("¿Desea jugar otra partida? (s/n): ").lower()

    mostrar_estadisticas(estadisticas, resumen, partidas_jugadas)

# Programa principal
while True:
    print("\n=== Menú Principal ===")
    print("1. Jugar")
    print("2. Reglas del juego")
    print("3. Ver estadísticas del último set de partidas")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- Menú de juego ---")
        print("1. Un solo jugador (contra la computadora)")
        print("2. Multijugador (2 jugadores)")
        print("3. Regresar al menú principal")
        modo = input("Elige un modo: ")
        if modo in ["1", "2"]:
            jugar(modo)
    elif opcion == "2":
        mostrar_reglas()
    elif opcion == "3":
        print("Primero debes jugar alguna partida para ver estadísticas.")
    elif opcion == "4":
        print("Saliendo del juego. ¡Gracias por jugar!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
