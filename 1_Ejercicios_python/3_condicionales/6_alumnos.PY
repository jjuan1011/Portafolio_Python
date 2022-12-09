
'''
EJERCICIO 6

Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

class Alumnos():
    def __init__(self):
        self.ingrese_nombre = str(input('Ingrese su Nombre => '))
        print('Si es hombre ingrese la letra => H')
        print('Si es mujer ingrese la letra => M')
        self.ingrese_sexo = str(input('Ingrese su sexo => '))
    
    def grupo_A(self):
        if self.ingrese_sexo.lower() == 'm':
            if self.ingrese_nombre.lower() < 'm':
                group = 'A'
            else: 
                group = 'B'
        else:
            if self.ingrese_nombre.lower() > "n":
                group = "A"
            else:
                group = "B"
                print("Tu grupo es " + group)

