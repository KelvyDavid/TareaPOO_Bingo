import random


class CartonBingo:
    def __init__(self):
        self.numeros = []
        self.limiteInferior = 1
        self.limiteSuperior = 101
        self.cantidadNumeros = 25
        self.cantFilas = 5
        self.dimFila = int(self.cantidadNumeros / self.cantFilas)
        self.generar_carton()

    def generar_carton(self):
        lista_numeros = random.sample(range(self.limiteInferior, self.limiteSuperior), self.cantidadNumeros)
        lista_numeros.sort()
        for i in range(self.cantFilas):
            fila = lista_numeros[i * self.dimFila:(i + 1) * self.dimFila]
            self.numeros.append(fila)

    def marcar_numero(self, numero):
        for i in range(self.cantFilas):
            for j in range(self.dimFila):
                if self.numeros[i][j] == numero:
                    self.numeros[i][j] = "X"

    def verificar_bingo(self):
        # Verificar filas
        for fila in self.numeros:
            if all(elemento == "X" for elemento in fila):
                return True
        # Verificar columnas
        for col in range(self.dimFila):
            if all(self.numeros[row][col] == "X" for row in range(self.cantFilas)):
                return True
        return False

    def mostrar_carton(self):
        for fila in self.numeros:
            print('\t'.join(map(str, fila)))
        print()


class Bingo:
    def __init__(self, jugadores):
        self.jugadores = [CartonBingo() for _ in range(jugadores)]
        self.num_sorteados = set()
        self.juego_terminado = False

    def mostrar_cartones(self):
        for i, jugador in enumerate(self.jugadores):
            print(f'CARTON DE BINGO DEL JUGADOR {i + 1}:')
            jugador.mostrar_carton()

    def sortear_numero(self):
        while True:
            numero_str = input('Introduce un número del para sortear: ')
            try:
                numero = int(numero_str)
                if 1 <= numero <= 101 and numero not in self.num_sorteados:
                    self.num_sorteados.add(numero)
                    print(f"Número sorteado: {numero}")
                    return numero
                else:
                    print(f"El número {numero} ya ha sido sorteado o no está en el rango permitido.")
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número válido.")

    def actualizar_cartones(self, numero):
        for jugador in self.jugadores:
            jugador.marcar_numero(numero)

    def verificar_bingo(self):
        for i, jugador in enumerate(self.jugadores):
            if jugador.verificar_bingo():
                print(f"¡Bingo! El jugador {i + 1} ha ganado.")
                jugador.mostrar_carton()
                self.juego_terminado = True
                return True
        return False

    def jugar(self):
        while not self.juego_terminado:
            numero = self.sortear_numero()
            self.actualizar_cartones(numero)
            self.mostrar_cartones()
            if self.verificar_bingo():
                break


def valida_cantidad(jugadores):
    try:
        entero_jugadores = int(jugadores)
        if entero_jugadores < 1:
            raise ValueError
        return True
    except ValueError:
        print('La cantidad de jugadores ingresados no es valida, favor ingresar un numero entero positivo.')
        return False


def jugar_bingo():
    print('***** TAREA DE PROGRAMACION ORIENTADA A OBJETOS *****')
    print('Ejercicio 2.- Implementación de un Bingo en python')
    print('Grupo 2: \nXIMENA GABRIELA CARDENAS TOALA \nJUAN CARLOS IZURIETA CISNEROS \nALAN ARIEL TAPIA BENITEZ \n'
          'DAVID KELVY TOMALA CIMARRA \nCRISTOPHER WILLIAM VERA AMAIQUEMA \n\n')
    print('***BIENVENIDO AL GRAN BINGO***\n')
    while True:
        cant_jugadores = input('Ingrese la cantidad de jugadores: ')
        if valida_cantidad(cant_jugadores):
            break
    sala_bingo = Bingo(int(cant_jugadores))
    sala_bingo.mostrar_cartones()
    sala_bingo.jugar()


if __name__ == '__main__':
    while True:
        jugar_bingo()
        continuar = input("¿Desea continuar jugando? (si/no): ").strip().lower()
        if continuar != 'si':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break