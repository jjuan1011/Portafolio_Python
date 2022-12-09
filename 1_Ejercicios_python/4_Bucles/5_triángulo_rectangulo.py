

'''
EJERCICIO 5

Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
'''

class Numero():
    def __init__(self):
        self.ingrese = int(input('Ingresa tu numero putito => '))
    
    def triangulo(self):
        for i in range(self.ingrese):
            print("*"*(i+1))


triangulo_rectangulo = Numero()
triangulo_rectangulo.triangulo()