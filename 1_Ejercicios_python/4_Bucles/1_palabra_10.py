

'''
EJERCICIO 1

Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

class Palabra():
    def __init__(self):
        self.word = str(input('Ingrese palabra => '))
    
    def impresion(self):
        for i in range(10):
            print(i)

imprimir = Palabra()
imprimir.impresion()