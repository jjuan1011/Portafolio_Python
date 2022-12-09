

'''
EJERCICIO 3

Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''

class Numeros():
    def __init__(self):
        self.num1 = int(input('Ingresa un numero putito => '))
        self.num2 = int(input('Ingresa otro número putito => '))
        self.ejecutar_operacion = self.num1 /  self.num2
    
    def operacion(self):
        if self.num2 == 0:
            return KeyError
        else:
            print(f'El resultado de la division es {self.ejecutar_operacion}')

resultado = Numeros()
print(resultado.operacion())
            
         
