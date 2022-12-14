

'''
EJERCICIO 1

Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
'''

class Cash_register():
    def __init__(self):
        self.price = float(input('Ingresa el precio correspondiente => '))
    
    def tax(self):
        self.tax_19_sum = self.price * 19 / 100
        self.tax_19 = self.price + self.tax_19_sum
        print('Valor total con iva 19% => ',self.tax_19)

    def discount(self):
        self.discount_20 = self.price * 20 / 100 
        self.final_price_20 = self.price - self.discount_20  + self.tax_19_sum
        print('El precio final con un descuento del 20% es = ',self.final_price_20)

    def final_price(self):
        self.dictionary = {}
        self.dictionary['Elemento'] = self.final_price_20
        print(self.dictionary)


result = Cash_register()
result.tax()
result.discount()
result.final_price()

