

'''
Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
'''

class Vocales():
    def __init__(self):
        self.word = input('Ingresa tu palabra caremondá => ')
        self.vocals = ["a","e","i","o","u"]
    
    def contador(self):
        for vocal in self.vocals: 
            self.times = 0    
            for letter in self.word:
                if letter == vocal:
                    self.times += 1
            print("La vocal " + vocal + " aparece " + str(self.times) + " veces")

contado = Vocales()
contado.contador()

