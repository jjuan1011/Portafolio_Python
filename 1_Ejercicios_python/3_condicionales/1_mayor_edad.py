
'''
EJERCICIO 1

Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''



class Listado():
    def __init__(self):
        self.invitado = int(input('Ingresa tu edad => '))
    
    def ingresa(self):
        if self.invitado >= 18:
            print('Puedes ingresar a la fiesta')
        else:
            print('Vete a casa a ver pocoyó')


invitado_ingresa = Listado()
print(invitado_ingresa.ingresa())
