
'''
EJERCICIO 9

Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
'''

class Bills():
    def __init__(self):
        self.accum_bill = {}
        self.request = ''
        self.request_2 = ''
        self.request_3 = ''

        
    def add(self):
        while self.request != 2:
            self.supplier_bill = str(input('Ingrese el proveedor de la factura => '))
            self.amount_bill = str(input('Ingrese valor a pagar seguido de una coma => '))
            self.accum_bill[self.supplier_bill] = self.amount_bill

            self.request = int(input('Para agregar una nueva factura ingrese = 1, para Consultar ingrese = 2, INGRESE => '))
    
    def consult(self):
        while self.request_2 != 2:
            self.consult_bill = str(input('Ingrese el proveedor que desea consultar => ')).lower()
            for i in self.accum_bill:
                if i in self.consult_bill:
                    print(self.accum_bill[i])
            
            self.request_2 = int(input('Para hacer una nueva busqueda ingrese = 1, para Pagar un factura ingrese = 2, INGRESE => '))

    def pay(self):
        while self.request_3 != 2:
            self.pay_bill = str(input('Ingrese el proveedor de la factura que desea pagar => ')).lower()
            for i in self.accum_bill:
                if i in self.pay_bill:
                    print('Se eliminará la siguiente factura => ' + self.pay_bill + self.accum_bill[i])
            self.delete = self.accum_bill.pop(self.pay_bill)
            print(self.delete)
            
            self.request_3 = int(input('Para hacer un Nuevo Pago ingrese = 1, para SALIR ingrese = 2, INGRESE => '))



paga = Bills()
paga.add()
paga.consult()
paga.pay()

# /////////////////////////////////////////////////////////////////////////////////////
facturas = {}
cobrado = 0
pendiente = 0
more = ''
while more != 'T':
    if more == 'A':
        clave = input('Introduce el número de la factura: ')
        coste = float(input('Introduce el coste de la factura: '))
        facturas[clave] = coste
        pendiente += coste
    if more == 'P':
        clave = input('Introduce el número de la factura a pagar: ')
        coste = facturas.pop(clave, 0)
        cobrado += coste
        pendiente -= coste
    print('Recaudado:', cobrado)
    print('Pendiente de cobro: ', pendiente)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')