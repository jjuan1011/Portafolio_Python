

'''
EJERCICIO 1

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
'''

class Asignaturas():
    def __init__(self):
        self.subjects = ["Matematicas", "Física", "Química", "Historia", "Lengua"]
        self.scores = []
    
    def almacena(self):
        for i in self.subjects:
            self.individual_score =  input("¿Qué nota has sacado en " + i + "?")
            self.scores.append(self.individual_score)
        for i in range(len(self.subjects)):
            print("En " + self.subjects[i] + " has sacado " + self.scores[i])
    
    # def promedio(self):
    #     self.suma = 0
    #     for x in range(len(self.scores)):
    #         self.suma = self.suma + x
    #         print(self.suma)

    #     self.promedio_final = self.suma / 5
    #     if self.promedio_final > 60:
    #         print('Pasaste el año ♥')
    #         print(f'Tu promedio Final es de {self.promedio_final}')
    #     else:
    #         print('Te tiraste el año Careverga :(')
    #         print(f'Tu promedio Final es de {self.promedio_final}')


materia = Asignaturas()
materia.almacena()
# materia.promedio()
