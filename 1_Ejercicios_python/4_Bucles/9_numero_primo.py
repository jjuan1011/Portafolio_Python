

'''
GASTOS

EJERCICIO 9

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''

class Primo():
    def __init__(self):
        self.ingrese = int(input('Ingresa un número => '))
    
    def verifica_primo(self):
        i = 2
        while self.ingrese % i != 0:
            i += 1
        if i == self.ingrese:
            print(str(self.ingrese) + " es primo")
        else:
            print(str(self.ingrese) + " no es primo")

numero_primo = Primo()
numero_primo.verifica_primo()