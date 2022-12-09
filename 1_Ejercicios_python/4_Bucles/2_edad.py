

'''
EJERCICIO 2

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

class Edad():
    def __init__(self):
        self.age = int(input('Ingresa tu edad => '))
    
    def años(self):
        for i in range(self.age):
            print(f'Tu edad es {i}')

edad = Edad()
edad.años()