'''
EJERCICIO 10 

Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
'''

payasos_vendidos = float(input('Ingrese el numero de payasos vendidos en el pedido del cual necesita información => '))
muñecas_vendidas = float(input('Ingrese el numero de muñecas vendidas en el pedido del cual necesita información => '))

peso_payaso = 112
peso_muñeca = 75

peso_paquete_payasos = payasos_vendidos * peso_payaso
print('__________________________________________________________________')
print('Tabla de información del pedido')
print(f'El peso del paquete de {payasos_vendidos} payasos vendidos es de => {peso_paquete_payasos} g')
peso_paquete_muñecas = muñecas_vendidas * peso_muñeca
print(f'El peso del paquete de {muñecas_vendidas} muñecas vendidas es de => {peso_paquete_muñecas} g')
print('__________________________________________________________________')
peso_paquete_completo = peso_paquete_payasos + peso_paquete_muñecas
print(f'El peso total es de => {peso_paquete_completo} g')
print('__________________________________________________________________')