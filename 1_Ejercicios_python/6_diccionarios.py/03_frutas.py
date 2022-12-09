

'''
Ejercicio 3

Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
'''

class Frutería():
    def __init__(self):
        self.fruber = {
            'platano': 5000,
            'manzana': 4500,
            'pera': 4100,
            'naranja': 3500,
        }
        print(self.fruber)

        self.fruit = ''
        self.fruit.lower()
        self.weight = ''
        self.request = ''
    
    def final_price(self):
        while self.request != 2:
            self.fruit = input('Ingresa la fruta que deseas llevar => ').lower()
            self.weight = float(input('Ingresa el peso del producto que deseas llevar => '))
            if self.fruit in self.fruber:
                print('Por un peso de ',self.weight, 'PAGAS', self.fruber[self.fruit]*self.weight, 'Pesos' )
            else:
                print(f'Lo sentimos la fruta {self.fruit} no se encuentra en el inventario')

            self.request = int(input('Si deseas averiguar otro producto Ingresa 1, Si deseas ir a caja ingresa 2 => '))
        print('Que tengas un lindo día mor')
        

        
canasta = Frutería()
canasta.final_price()


        
