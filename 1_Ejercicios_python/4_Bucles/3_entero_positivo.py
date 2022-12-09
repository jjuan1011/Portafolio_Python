

'''
EJERCICIO 3

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

class Numeros():
    def __init__(self):
        self.user_number = int(input('Ingresa un numero => '))
    
    def impares(self):
        for i in range(1, self.user_number + 1, 2):
           print(i, end=',')

impar = Numeros()
impar.impares()