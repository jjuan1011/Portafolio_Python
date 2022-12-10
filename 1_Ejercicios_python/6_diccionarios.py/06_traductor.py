
'''
EJERCICIO 8

Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
'''

class Dictionary():
    def __init__(self):
        self.keywords = {}
        self.request = ''
    
    def solution(self):
        while self.request != 2:
            self.word = input('Ingresa la palabra a traducir => ')
            self.traduction = input('Ingresa la traducción de dicha palabra => ') 
            self.keywords[self.word] = self.traduction
            print(self.keywords)

            self.request = int(input('Para continuar agregando palabras ingresa => 1 <= para salir ingresa => 2 <= _ =>>> '))
        
        self.traduce = input('Ingresa el contenido que quieres traducir según el diccionario => ')
        for i in self.keywords:
            if i in self.traduce:
                print(self.keywords[i])
            

traduce = Dictionary()
traduce.solution()

