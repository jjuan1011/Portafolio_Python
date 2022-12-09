

'''
EJERCICIO 7

Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000000€	5%
Entre 10000000 y 20000000	15%
Entre 20000000 y 35000000	20%
Entre 35000000 y 60000000	30%
Más de 60000000	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''


class Renta():
    def __init__(self):
    
        print('===============================RENTA PERSONAS NATURALES 2023================================')
        self.renta_user = int(input('______________________Digite sus ingresos Anuales => '))
    
    def ingresos(self):
        if self.renta_user < 10000000:
            self.calculo = self.renta_user * 5 / 100
            print('____________________________________________________________________')
            print('Tu tasa impositiva es del 5% de acuerdo a tu rango de ingresos  $$$')
            print(f'Es decir que te corresponde una contribución de {self.calculo}  Cop')
        elif self.renta_user >= 10000000 and self.renta_user <= 20000000:
            self.calculo = self.renta_user * 15 / 100
            print('____________________________________________________________________')
            print('Tu tasa impositiva es del 15% de acuerdo a tu rango de ingresos  $$$')
            print(f'Es decir que te corresponde una contribución de {self.calculo}  Cop')
        elif self.renta_user >= 20000001 and self.renta_user <= 35000000:
            self.calculo = self.renta_user * 20 / 100
            print('____________________________________________________________________')
            print('Tu tasa impositiva es del 20% de acuerdo a tu rango de ingresos  $$$')
            print(f'Es decir que te correspone una contribución de {self.calculo} Cop')
        elif self.renta_user >= 35000001 and self.renta_user <= 60000000:
            self.calculo = self.renta_user * 30 / 100
            print('____________________________________________________________________')
            print('Tu tasa impositiva es del 30% de acuerdo a tu rango de ingresos  $$$')
            print(f'Es decir que te correspone una contribución de {self.calculo} Cop')
        elif self.renta_user >= 60000001:
            self.calculo = self.renta_user * 40 / 100
            print('____________________________________________________________________')
            print('Tu tasa impositiva es del 45% de acuerdo a tu rango de ingresos  $$$')
            print(f'Es decir que te correspone una contribución de {self.calculo} Cop')
        

            
        



usuario = Renta()
print(usuario.ingresos())
