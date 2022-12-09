

'''
EJERCICIO 6

Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''

class Tablas():
    def __init__(self):
        self.ingrese_valor = int(input('Digita la tabla que deseas consultar ♥ => '))
    
    def tabla_multiplicar(self):
        for i in range(10):
            i *= self.ingrese_valor
            print(i)
    

multiplicador = Tablas()
multiplicador.tabla_multiplicar()
