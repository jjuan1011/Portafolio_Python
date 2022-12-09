
'''
EJERCICIO 9

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
'''


class Inversion():
    def __init__(self):

        self.productos_banco_3 = ['CDT', 'Fondo Porvenir', 'Fondo Colpatria', 'Bono de Estado']
        self.productos_banco_5 = ['Fondo Argos', 'Fondo Seguros', 'Fondo Colpensiones', 'Acciones Grupo Aval']
        self.productos_banco_7 = ['Acciones Colpatria', 'Acciones Bolivar', 'Acciones D1', 'Acciones BBVA']
        self.productos_banco_10 = ['Acciones Bancolombia', 'Acciones Davivienda', 'Acciones Ara', 'Acciones Jumbo']
        self.productos_banco_15 = ['Acciones Metro', 'Acciones Exito', 'Acciones Royal Films', 'Acciones Cruz Verde']
        self.productos_banco_25 = ['Acciones Bella Piel', 'Acciones Jillete', 'Acciones Porseguros', 'Acciones Emergentes']

        print('=================================== INVERSIÓN ANUAL ==========================================')
        print('___________________________________ Tabla de Interés _________________________________________')
        print('Para elegir alguna opción ingrese el número relacionado al porcentaje\n EJEMPLO: Para el interés del 3% ingrese => 3, Para el interés del 5% ingrese => 5 y así con el interés que desee. ')
        print('______________________________________________________________________________________________')
        print('INTERÉS DEL 3%')
        print('Activos de inversión para esta categoría : ')
        print('__________________________________________')
        for i in self.productos_banco_3:
                print(i)
        print('______________________________________________________________________________________________')
        print('INTERÉS DEL 5% ANUAL')
        print('Activos de inversión para esta categoría : ') 
        print('__________________________________________')
        for i in self.productos_banco_5:
                print(i)
        print('______________________________________________________________________________________________')
        print('INTERÉS DEL 7% ANUAL')
        print('Activos de inversión para esta categoría : ')
        print('__________________________________________')
        for i in self.productos_banco_7:
                print(i)
        print('______________________________________________________________________________________________')
        print('INTERÉS DEL 10% ANUAL')
        print('Activos de inversión para esta categoría : ')
        print('__________________________________________')
        for i in self.productos_banco_10:
                print(i)
        print('______________________________________________________________________________________________')
        print('INTERÉS DEL 15% ANUAL')
        print('Activos de inversión para esta categoría : ')
        print('__________________________________________')
        for i in self.productos_banco_15:
                print(i)
        print('______________________________________________________________________________________________')
        print('INTERÉS DEL 25% ANUAL')
        print('Activos de inversión para esta categoría : ')
        print('__________________________________________')
        for i in self.productos_banco_25:
                print(i)
        print('______________________________________________________________________________________________')


        self.usser = float(input(' $$$$$$$$$     Ingresa aquí tu monto de inversión => '))
        self.usser_interes = float(input(' $$$$$$$$$     Ingresa aquí el interés sobre tu inversión => '))
        self.usser_años = float(input(' $$$$$$$$$     Ingresa aquí La cantidad de años a la que quieres dejar tu inversión => '))
    
    def interes(self):
        if self.usser_interes == 3:
            self.usser *= self.usser_interes / 100
            self.final = self.usser * self.usser_años
            print(f'El retorno sobre tu inversión será de {self.final}')
        elif self.usser_interes == 5:
            self.usser *= self.usser_interes / 100
            self.final = self.usser * self.usser_años
            print(f'El retorno sobre tu inversión será de {self.final}')
        elif self.usser_interes == 7:
            self.usser *= self.usser_interes / 100
            self.final = self.usser * self.usser_años
            print(f'El retorno sobre tu inversión será de {self.final}')
        elif self.usser_interes == 10:
            self.usser *= self.usser_interes / 100
            self.final = self.usser * self.usser_años
            print(f'El retorno sobre tu inversión será de {self.final}')
        elif self.usser_interes == 15:
            self.usser *= self.usser_interes / 100
            self.final = self.usser * self.usser_años
            print(f'El retorno sobre tu inversión será de {self.final}')
        elif self.usser_interes == 25:
            self.usser *= self.usser_interes / 100
            self.final = self.usser * self.usser_años
            print(f'El retorno sobre tu inversión será de {self.final}')
        else:
            print('Elige una opción Correcta')
            



inversor = Inversion()
print(inversor.interes())

#  self.gananacia_interes = self.usser * self.usser_interes / 100
#             self.final = self.gananacia_interes * self.usser_años
#             print(f'El retorno sobre tu inversión será de {self.final}')