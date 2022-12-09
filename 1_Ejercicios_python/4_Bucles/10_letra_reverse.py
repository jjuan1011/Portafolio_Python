

'''
EJERCICIO 10

Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''

class Palabra():
    def __init__(self):
        self.ingrese = input('Ingresa tu puta palabra => ')
    
    def reverse(self):
        for i in range(len(self.ingrese)-1, -1, -1):
            print(self.ingrese[i])

palabrita = Palabra()
palabrita.reverse()

