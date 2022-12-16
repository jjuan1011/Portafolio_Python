

'''
Crear un programa en el que un usuario pueda ingresar a una pagina web de compras

**************************
1. Clases y funciones
2. Iteraciones
3. Agregar elementos a listas, tuplas, diccionarios
4. Pedir datos a usuarios y ponerlos en un formato unico aceptable para que el programa busque  entre sus datos
5. Realizar operaciones matemáticas
6. condicionales
7. bucles
'''
import random
class Store():
    def __init__(self):

        self.request = ''
        self.exit_or_continue_man = ''
        self.exit_or_continue_girl = ''
        self.buy_cest = []
        self.random_number = [2923,30393,4478,3725,38374,2826,38474,39374,923746,83465,93746,938743,9387347,9338,2937,46347,2646,5979,2647,69696,38464,4856]

        self.man = {
            'camiseta negra':50000, 'camiseta blanca':55000, 'camiseta roja':55000, 'Camiseta azul ':60000,'pantalon negro':50000, 'pantalon blanco':150000, 'pantalon rojo':55000, 'pantalon azul':110000,
            'saco negro':150000, 'saco blanco':155000, 'saco rojo':135000, 'saco azul':110000,'zapatos negros':350000, 'zapatos blancos':355000, 'zapatos rojos':275000, 'zapatos azules':285000
        }

        self.girl = {
            'camiseta negra':50000, 'camiseta blanca':55000, 'camiseta roja':55000, 'Camiseta azul ':60000,'pantalon negro':50000, 'pantalon blanco':150000, 'pantalon rojo':55000, 'pantalon azul':110000,
            'saco negro':150000, 'saco blanco':155000, 'saco rojo':135000, 'saco azul':110000,'zapatos negros':350000, 'zapatos blancos':355000, 'zapatos rojos':275000, 'zapatos azules':285000
        }
    
    def Central(self):
        while self.request != 'no':
            print('========================= BIENVENIDO A ZARA ========================')
            print('- Para ver el menú de hombres ingresa => H \n - Para ver el menú de chicas ingrese => C \n - Para ver el carrito de la compra ingresa => F')
            self.usser_election = input('Ingresa la opción según lo que deseas hacer => ').lower()

            if self.usser_election == 'h':
                while self.exit_or_continue_man != 1:
                    print(self.man)
                    self.add_element_man = input('Ingrese el elemento que desea agregar al carrito => ').lower()
                    for i in self.man:
                        if i in self.add_element_man:
                            self.man[i] #Valor de la iteración ej: precio de articulo
                        # self.buy_cest[self.add_element_man] = self.man[i] # Clave valor 
                    self.exit_or_continue_man = int(input('Para salir ingrese => 1, para seguir en la sección de hombres ingrese => 2  INGRESE SU OPCIÓN =>>> '))
                
            elif self.usser_election == 'c':
                while self.exit_or_continue_girl != 1:
                    print(self.girl)
                    self.add_element_girl = input('Ingrese el elemento que desea agregar al carrito => ').lower()
                    for i in self.girl:
                        if i in self.add_element_girl:
                            self.girl[i] #Valor de la iteración ej: precio de articulo
                            # self.buy_cest[self.add_element_girl] = self.girl[i] # Clave valor 
                    self.exit_or_continue_girl = int(input('Para salir ingrese => 1, para seguir en la sección de mujere1s ingrese => 2 INGRESE SU OPCIÓN =>>> '))

            self.request = input('Para continuar comprando ingresa = si, para ir a pagar ingresa => no  INGRESA TU OPCIÓN =>>> ').lower()
        

            # elif self.usser_election == 'f':
            #     print(self.buy_cest)
            #     self.total_price = self.man[i] + self.girl[i]
            #     print(f'El valor total de su carrito es de {self.total_price}')

        
    def pay(self):
        print('======================= Elija su método de pago =======================')
        print('Valor a pagar 000000 pesos')
        self.usser_pay = str(input(' - Tarjeta de crédito = 01 \n - Tarjeta débito = 02 \n - Efectivo = 03  \n INGRESE EL CÓDIGO DE LA OPCIÓN QUE DESEA => ' ))
        if self.usser_pay == '01':
            input('- Ingrese el número de la tarjeta =>>> ')
            input('- Ingrese CCV de la tarjeta =>>> ')
            input('- Ingrese F/v =>>> ')
            input('Ingrese el número de cuotas => ')
            input('====== PAGO EXITOSO ======')
        elif self.usser_pay == '02':
            input('- Ingrese el número de la tarjeta =>>> ')
            input('- Ingrese CCV de la tarjeta =>>> ')
            input('- Ingrese F/v =>>> ')
            input('- CUENTA AHORROS  ')
            input('====== PAGO EXITOSO ======')
        elif self.usser_pay == '03':
            self.code = random.choice(self.random_number)
            print(f'Codigo Generado  {self.code}')
            print('Dale este codigo al asesor del punto de pago :) ')
        
        
final = Store()
final.Central()
final.pay()



