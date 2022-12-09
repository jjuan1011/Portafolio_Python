

'''
EJERCICIO 7

Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
'''

class Triangulo():
    def __init__(self):
        self.ingrese = int(input('Ingresa un número putito => '))
    
    def operacion(self):
        for i in range(self.ingrese):
            print("*"*(i+1))



objeto = Triangulo()
objeto.operacion()
