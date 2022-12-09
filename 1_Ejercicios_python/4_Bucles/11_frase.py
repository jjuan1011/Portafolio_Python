

'''
Ejercicio 12

Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''

class Frase():
    def __init__(self):
        self.sentence = input('Ingrese una frase => ')
        self.letter = input('Ingrese una letra x => ')
        self.contador = 0
    
    def analisis(self):
        for i in self.sentence:
            if i == self.letter:
                self.contador += 1
        print(f'La letra {self.letter}, aparece {self.contador} veces en la frase "{self.sentence}"')
    
analisis_resutados = Frase()
analisis_resutados.analisis()


