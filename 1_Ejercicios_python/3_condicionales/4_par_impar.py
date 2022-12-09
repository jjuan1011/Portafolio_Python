
'''
EJERCICIO 4

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''

class Par_impar():
    def __init__(self):
        self.entero = int(input('Ingresa un número entero => '))
    
    def comprobacion(self):
        if self.entero % 2 == 0:
            print(f'El número {self.entero} es par')
        else:
            print(f'El numero {self.entero} es impar')

comprobacion_final = Par_impar()
print(comprobacion_final.comprobacion())
