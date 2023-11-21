"""Piedra, papel o tijeras!


Juego de piedra, papel o tijeras hecho en Python.
"""

import random


def eleccion_computadora():
    """Obtiene una opción aleatoria para que la computadora la use."""

    computadora = random.choice(opciones)
    return computadora


def eleccion_usuario():
    """Obtiene la opción que el jugador usará."""

    usuario = str(input("Selecciona lo que quieres jugar en esta ronda: Piedra, papel o tijeras.\n"))
    usuario = usuario.lower()
    if usuario in opciones:
        return usuario
    else:
        raise Exception("Tu elección no es válida. Verifica errores tipográficos e intenta nuevamente.")


def ejecutar_juego():
    """Inicia y maneja el juego de principio a fin."""

    rondas = 3
    victoria_usuario = 0
    victoria_computadora = 0

    print("*" * 15)
    print("El juego comenzará ahora.")
    print("*" * 15)
    
    while True:

        computadora = eleccion_computadora()
        usuario = eleccion_usuario()
        print(f"{usuario} vs {computadora}, ")
            

        if usuario == computadora:

            rondas -= 1
            print(f"""

            ¡Empate!
            Ambos han elegido {usuario}
            {rondas} restantes.

            """)


        if (usuario == "tijeras" and computadora == "papel") or (usuario == "piedra" and computadora == "tijeras") or (usuario == "papel" and computadora == "piedra"):
        
            rondas -= 1
            victoria_usuario += True

            print(f"""
            
            Has ganado esta ronda.
            ¡{usuario} vence a {computadora}!
            {rondas} restantes.

            """)


        if (computadora == "tijeras" and usuario == "papel") or (computadora == "piedra" and usuario == "tijeras") or (computadora == "papel" and usuario == "piedra"):
    
            rondas -= 1
            victoria_computadora += True
            
            print(f"""
            
            Has perdido esta ronda.
            ¡{computadora} vence a {usuario}!
            {rondas} restantes.

            """)

        
        if rondas <= 0:
            if victoria_usuario == victoria_computadora:
                print("Es un empate, has terminado el juego con la misma cantidad de puntos.")
                break
            if victoria_computadora > victoria_usuario:
                print(f"Partida terminada. El ganador es la computadora con {victoria_computadora} puntos.")
                break
            if victoria_computadora < victoria_usuario:
                print(f"Partida terminada. ¡Eres el ganador con {victoria_usuario} puntos!")
                break


if __name__ == "__main__":
    # Opciones de elección globales.
    opciones = ("piedra", "papel", "tijeras")
    ejecutar_juego()
