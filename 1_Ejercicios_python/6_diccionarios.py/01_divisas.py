

'''
EJERCICIO 1

Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''

class Divisas():
    def __init__(self):
        self.dictionary = {
            'euro': '€',
            'dollar': '$',
            'yen': '¥',
        }
        self.write = ''
        self.write.lower()
        self.re_write = ''

    def mensaje(self):
        while self.re_write != 2:
            self.write = input('Ingrese una divisa para ver si simbolo => ')
            if self.write == 'euro':
                print('El simbolo de la divisa Euro es (€)')
            elif self.write == 'dollar':
                print('El simbolo de la divisa dollar es ($)')
            elif self.write == 'yen':
                print('El simbolo de la divisa Yen es (¥)')
            else:
                print('Ingrese una opción válida ;(')
            self.re_write = int(input('Para ver otro simbolo de otra divisa ingresa 1, para salir ingresa 2 => '))
        print('Lindo día perra')
               
divisa = Divisas()
divisa.mensaje()