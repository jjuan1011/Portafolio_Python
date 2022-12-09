

'''
Ejercicio 4

Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''

class Loteria():
    def __init__(self):
        self.lista = []
        for i in range(6):
            self.lista.append(int(input('Ingrese los números ganadores de la lotería => ')))
        self.lista.sort()
        print("Los números ganadores son " + str(self.lista))
 

numeros_ganadores = Loteria()
