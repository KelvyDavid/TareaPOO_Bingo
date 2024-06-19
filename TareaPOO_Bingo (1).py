""" TAREA DE PROGRAMACION ORIENTADA A OBJETOS
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
"""
#La libreria random permite generar los numeros aleatorios que se imprimiran en el carton de bingo, 
# asi como el numero a sortear.
import random


#La clase cartonBingo permite crear los cartones de bingo
class cartonBingo:

    #Atributos del carton de bingo
    def __init__(self):
        self.numeros = []
        self.limiteInferior = 1
        self.limiteSuperior = 76
        self.cantidadNumeros = 25
        self.cantFilas = 5
        self.dimFila = int(self.cantidadNumeros / self.cantFilas)

    #Genera una lista de números aleatorios en una matriz de 5*5
    def generarCarton(self):
        listaNumeros = random.sample(range(self.limiteInferior, self.limiteSuperior), self.cantidadNumeros)
        for i in range(self.cantFilas):
            fila = listaNumeros[i * self.dimFila:(i + 1) * self.dimFila]
            fila = [str(numero) for numero in fila]
            self.numeros.append(fila)

    #Retorna los números del cartón
    def mostrarDatos(self):
        return self.numeros


#La clase bingo permite crear y gestionar la sala de bingo
class bingo(cartonBingo):

    #Genera un cartón de bingo para el número de jugadores
    def __init__(self, jugadores):
        super().__init__()
        self.jugadores = []
        self.numSorteados = []
        for i in range(jugadores):
            self.carton = cartonBingo()
            self.carton.generarCarton()
            numCarton = self.carton.mostrarDatos()
            self.jugadores.append([f'JUGADOR {i + 1}', numCarton])

    #Muestra el cartón de bingo de cada uno de los jugador
    def mostrarCarton(self):
        for jugador in self.jugadores:
            print(f'Carton del {jugador[0]}')
            self.marcarNumero(jugador)

    #Solicita al usuario que presione enter para sortear un número,
    #generando un número aleatorio que no se haya repetido
    def sortearNumero(self):
        input('Presiona enter para enter para sortear un numero....')
        numero = 0
        while numero in self.numSorteados or numero == 0:
            numero = str(random.randint(self.carton.limiteInferior, self.carton.limiteSuperior))
        self.numSorteados.append(numero)
        print(f'El numero sorteado es: {numero}')
        return numero

    #Actualiza los cartones de los jugadores reemplazando el número sorteado con una "X"
    def actualizarCarton(self, numero):
        for jugador in self.jugadores:
            for lista in jugador[1]:
                for i in lista:
                    if numero == i:
                        indice = lista.index(i)
                        lista[indice] = 'X'
                        print(f'Se ha encontrado el numero sorteado en el carton del {jugador[0]}:')
                        self.marcarNumero(jugador)

    #Muestra los cartones que contengan el numero sorteado, ya actualizados
    def marcarNumero(self, jugador):
        for lista in jugador[1]:
            print('\t'.join(lista))
        print('\n')

    #Verifica si algún jugador ha completado una fila o columna marcado con una "X"
    def verificarBingo(self):
        # Verificar filas
        for jugador in self.jugadores:
            for fila in jugador[1]:
                if all(elemento == "X" for elemento in fila):
                    return jugador
        # Verificar columnas
        for col in range(self.carton.dimFila):
            for jugador in self.jugadores:
                if all(jugador[1][row][col] == "X" for row in range(self.carton.cantFilas)):
                    return jugador
        return False


#Valida que el número de jugadores sea un entero positivo
def validaCantidad(jugadores):
    try:
        int(jugadores)
        enteroJugadores = int(jugadores)
        if enteroJugadores < 1:
            raise ValueError
        elif enteroJugadores / float(jugadores) != 1:
            raise ValueError
        return True
    except ValueError:
        print('La cantidad de jugadores ingresados no es valida, favor ingresar un numero entero positivo.')
        print('intente nuevamente......')


#Funciones de juego
def jugarBingo():
    print('***** TAREA DE PROGRAMACION ORIENTADA A OBJETOS *****')
    print('Ejercicio 2.- Implementación de un Bingo en python')
    print('Grupo 2: \nXIMENA GABRIELA CARDENAS TOALA \nJUAN CARLOS IZURIETA CISNEROS \nALAN ARIEL TAPIA BENITEZ \n'
          'DAVID KELVY TOMALA CIMARRA \nCRISTOPHER WILLIAM VERA AMAIQUEMA \n\n')
    print('***BIENVENIDO AL GRAN BINGO***\n')
    #solicita al usuario el numero de jugadores, verificando que sea un número entero positivo
    while True:
        cantJugadores = input('Ingrese la cantidad de jugadores: ')
        if validaCantidad(cantJugadores):
            break
    #Muestra los cartones de bingo para cada jugador
    print('\nCARTONES DE BINGO GENERADOS PARA CADA JUGADOR\n')
    salaBingo = bingo(int(cantJugadores))
    salaBingo.mostrarCarton()
    #Ciclo repetitivo donde se sortean números y se actualizan los cartones
    while True:
        numeroSorteado = salaBingo.sortearNumero()
        salaBingo.actualizarCarton(numeroSorteado)
        verificacionBingo = salaBingo.verificarBingo()
        if verificacionBingo != False:
            #Si hay un ganador,muetra en pantalla el mensaje de victoria y muestra el cartón del ganador
            print(f'Bingo!!!!!! El {verificacionBingo[0]} ha ganado.')
            salaBingo.marcarNumero(verificacionBingo)
            break


# A partir de este punto inicia la ejecucion del programa.
if __name__ == '__main__':
    while True:
        jugarBingo()

        #Solicita al usuario si desea continuar jugando
        while True:
            continuar = input("¿Desea continuar jugando? (si/no): ").strip().lower()
            if continuar in ['si', 'no']:
                break
            else:
                print('Favor ingrese una opcion valida, intente nuevamente.....')
        if continuar == 'no':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        elif continuar == 'si':
            print('\n\n\n')
            pass
