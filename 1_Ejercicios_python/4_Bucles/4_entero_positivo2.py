

'''
EJERCICIO 4

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''

class Numero():
    def __init__(self):
        self.ingrese = int(input('Ingresa un número pinche usuario vergo => '))
    
    def regresiva(self):
        for i in range(self.ingrese,-1, -1):
            print(i, end=',')
        

numero = Numero()
numero.regresiva()