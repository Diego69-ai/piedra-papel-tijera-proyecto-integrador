import random

# Opciones válidas
opciones = ["piedra", "papel", "tijera"]

# Variable para guardar el resultado de la última partida
ultima_partida = None

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

# Menú principal
while True:
    print("\n--- Menú Principal ---")
    print("1. Contra la computadora")
    print("2. Multijugador (2 jugadores)")
    print("3. Ver estadísticas de la última partida")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Contra la computadora
        jugador = input("Elige piedra, papel o tijera: ").lower()
        while jugador not in opciones:
            jugador = input("Opción inválida. Intenta de nuevo: ").lower()

        computadora = random.choice(opciones)
        print("La computadora eligió:", computadora)

        resultado = determinar_ganador(jugador, computadora)
        if resultado == "Empate":
            print("¡Empate!")
        elif resultado == "Jugador 1":
            print("¡Ganaste!")
        else:
            print("Perdiste :(")

        ultima_partida = resultado

    elif opcion == "2":
        # Multijugador
        jugador1 = input("Jugador 1, elige piedra, papel o tijera (no se mostrará): ").lower()
        while jugador1 not in opciones:
            jugador1 = input("Opción inválida. Intenta de nuevo: ").lower()

        print("\n" * 50)  # limpia pantalla (truco básico)
        jugador2 = input("Jugador 2, elige piedra, papel o tijera (no se mostrará): ").lower()
        while jugador2 not in opciones:
            jugador2 = input("Opción inválida. Intenta de nuevo: ").lower()

        resultado = determinar_ganador(jugador1, jugador2)
        if resultado == "Empate":
            print("¡Empate!")
        elif resultado == "Jugador 1":
            print("¡Ganador: Jugador 1!")
        else:
            print("¡Ganador: Jugador 2!")

        ultima_partida = resultado

    elif opcion == "3":
        # Ver estadísticas
        if ultima_partida is None:
            print("No se ha jugado ninguna partida todavía.")
        else:
            print("Último resultado:", ultima_partida)

    elif opcion == "4":
        print("Saliendo del juego. ¡Gracias por jugar!")
        break

    else:
        print("Opción inválida, intenta de nuevo.")
