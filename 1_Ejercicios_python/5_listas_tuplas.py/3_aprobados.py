
'''
EJERCICIO 6

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''

class Asignaturas():
    def __init__(self):
        self.asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
        self.lista_notas = []

        for i in self.asignaturas:
            self.notas = float(input(f'Ingrese la Nota sacada en {i} => '))

            if self.notas >= 5:
                self.lista_notas.append(i)

    def reprobadas(self):
        for i in self.lista_notas:
            self.asignaturas.remove(i)
            print('Debes Nivelar estas asignaturas o de lo contrario perderás el año putito ;(')
        print(f"Debes Nivelar =>  {self.asignaturas}")

notas = Asignaturas()
notas.reprobadas()


