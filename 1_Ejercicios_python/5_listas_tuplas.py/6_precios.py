

'''
Ejercicio 10
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
'''

class Precios():
    def __init__(self):
        self.prices = [50,75,46,22,80,65,8]
        self.min = self.max = self.prices[0]

    def final(self):
        for i in self.prices:
            if i < self.min:
                self.min = i
            elif i > self.max:
                self.max = i
        print('El precio minimo es => '+ str(self.min))
        print('El precio máximo es => ' + str(self.max))

final_prices = Precios()
final_prices.final()
