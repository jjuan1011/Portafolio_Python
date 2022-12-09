

'''
EJERCICIO 5

Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a 1.000.000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''

class Tributacion():
    def __init__(self):
        print('=========================================================')
        print('    TABLA DE TRIBUTACION PERSONAS NATURALES AÑO 2023     ')
        print('=========================================================')
        self.edad = int(input('Ingresa tu edad => '))
        self.ingresos = float(input('Ingresa tus ingresos mensuales => '))
    
    def tributante(self):
        if self.edad >= 18 and self.ingresos >= 1000000:
            print('_____________________________________________________________________')
            print('\nEres una persona Natural que está obligada a Tributar por el gobierno de Colombia, por su condición de mayoría de edad, siempre y cuando cumpla los ingresos mínimos de tributante')
            print('_____________________________________________________________________')
            print('De acuerdo a la política de ingresos mínimos de tributación usted debe corresponer al Gobierno De Colombia con una contribución del 10% de sus ingresos')
            print('_____________________________________________________________________')
        else:
            print('De acuerdo a la política de Excepción físcal para personas sin ingresos, O de edad menor a 18, No será contribuyente mientras mantenga dicha Situación Financiera y/o Natural')
            print('_____________________________________________________________________')



tributacion = Tributacion()
print(tributacion.tributante())
