''' TAREA DE PROGRAMACION ORIENTADA A OBJETOS
GRUPO 2 - AULA C3

EJERCICIO 2: Implementación de un Bingo en Python

Descripción: Se solicita diseñar e implementar un sistema simple de Bingo utilizando el
paradigma de Programación Orientada a Objetos en Python. El sistema debe ser capaz de
generar cartones de bingo para los n jugadores, sortear números de forma aleatoria y
marcar los números en los cartones correspondientes. Adicionalmente, deberá verificar si
algún jugador ha completado un Bingo (una línea completa, ya sea horizontal o vertical).

Requisitos:

Clase CartonBingo: Esta clase representará cada cartón de Bingo. Deberá contener una
matriz (lista de listas en Python) que represente los números del cartón. Cada cartón debe
generarse con números aleatorios no repetidos dentro de un rango definido (por ejemplo,
del 1 al 75).

Clase Bingo: Esta clase será el núcleo del juego. Deberá manejar:
• La generación de números aleatorios para el sorteo.
• La asignación de cartones a los jugadores.
• La actualización de los cartones de los jugadores cada vez que se sortea un número.
• La verificación de la condición de victoria (Bingo).

Métodos importantes:
• generar_carton(): genera los n cartones para el bingo
• marcar_numero(): marca con X los números que coinciden en los cartones
• mostrar_carton(): muestra los cartones (inicial y final)
• sortear_numero(): selecciona un número al azar que no haya sido sorteado previamente.
• actualizar_carton(numero): marca el número sorteado en los cartones de los jugadores si 
  este se encuentra en ellos.
• verificar_bingo(): verifica si algún cartón cumple con la condición de Bingo. 

Interacción con el Usuario: 
Implementar una interfaz simple por consola que permita:
• Crear un juego de Bingo con una cantidad específica de jugadores (y por ende, de
cartones).
• Iniciar el sorteo de números y mostrar los cartones actualizados después de cada
número sorteado.
• Anunciar el ganador del juego una vez se cumpla la condición de Bingo.
'''

class cartonBingo:
    def __init__(self, jugadores):
        self.cantidadJugadores= jugadores
        self.numeros = []
        
    def generarCarton():
        pass

    def mostrarCarton():
        pass

    def actualizarCarton():
        pass

class bingo:
    def __init__(self, jugadores):
        self.cantidadJugadores= jugadores
        
    def sortearNumero():
        pass

    def marcarNumero():
        pass

    def verificarBingo():
        pass
    

def validaCantidad(jugadores):
    try:
        int(jugadores)
        enteroJugadores= int(jugadores)
        if enteroJugadores<1:
            raise ValueError
        elif enteroJugadores/float(jugadores) != 1:
            raise ValueError
        return True
    except ValueError:
        print('La cantidad de jugadores ingresados no es valida, favor ingresar un numero entero positivo.')
        print('intente nuevamente......')

# A partir de este punto inicia la ejecucion del programa.
if __name__== '__main__':
    print('***** TAREA DE PROGRAMACION ORIENTADA A OBJETOS *****')
    print('Ejercicio 2.- Implementación de un Bingo en python')
    print('Grupo 2: \nXIMENA GABRIELA CARDENAS TOALA \nJUAN CARLOS IZURIETA CISNEROS \nALAN ARIEL TAPIA BENITEZ \n'
          'DAVID KELVY TOMALA CIMARRA \nCRISTOPHER WILLIAM VERA AMAIQUEMA \n\n')
    print('***BIENVENIDO AL GRAN BINGO***\n')
    while True:
        cantJugadores = input('Ingrese la cantidad de jugadores: ')
        if validaCantidad(cantJugadores):
            break
    rondaBingo= cartonBingo(cantJugadores)
    rondaBingo.generarCarton()