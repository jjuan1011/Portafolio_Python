

'''
Ejercicio 6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario, este pondrá clave y valor. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''

class Information():
    def __init__(self):
        self.person = {}
        self.request = ""
    
    def solution(self):
        while self.request != 2:
            self.key = input('Ingresa el dato que quieres saber de la persona => ')
            self.value = input(self.key + ': ')
            self.person[self.key] = self.value
            print(self.person)
            self.request = int(input('Si deseas agregar otro dato ingresa => 1, para salir ingresa => 2. INGRESA => '))
            
        print('Adios perra')

info = Information()
info.solution()
            
