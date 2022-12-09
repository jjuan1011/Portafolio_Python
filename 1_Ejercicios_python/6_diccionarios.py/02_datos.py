

'''
EJERCICIO 2

Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''

class Information():
    def __init__(self):

        self.name = str(input('Ingresa tu nombre => '))
        self.age = str(input('Ingresa tu edad => '))
        self.direction = str(input('Ingresa de dirección => '))
        self.phone = str(input('Ingrese su número de telefono => '))

        self.dicctionary = {
            'Nombre': self.name,
            'Edad': self.age,
            'Dirección':self.direction,
            'Número Telefono':self.phone,
        }

        print(f'Tu nombre es {self.name}, Tienes {self.age} años, Tienes tu domicilio en la dirección {self.direction}, Tu número de contacto es: {self.phone}')
        
        print(self.dicctionary)

information = Information()
