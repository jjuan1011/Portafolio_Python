

'''
EJERCICIO 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
'''

class Cesta_compras():
    def __init__(self):
        self.cest = {}
        self.request = ""        
        
    
    def carrito(self):
        while self.request != 'no':
            self.key_product = input('Ingrese el artículo => ')
            self.value_price = float(input( self.key_product + ": "))
            self.cest[self.key_product] = self.value_price 
            print(self.cest)
            self.request = input('Quiere añadir un nuevo producto si / no => ').lower()
        self.cost = 0
        for self.key_product, self.value_price in self.cest.items():
            print(self.key_product, '\t' ,self.value_price )
            self.cost += self.value_price
        print('Costo de su carrito', self.cost)


cost = Cesta_compras()
cost.carrito()


