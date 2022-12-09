

'''
EJERCICIO 12

Una panadería vende barras de pan a 3.49€ cada una. El pan que no es Del día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
'''

pan = 3.49
descuento = 60 / 100

pan_viejo = pan * descuento

print("_______________________________________________________________")
float(input('Ingresa el numero de barras vendidas el día de hoy => '))
print('El precio de la barra de pan fresco es de 3.49 $ ')
print('              ========== ¡¡¡OFERTA!!! ==========                 ')
print('¡¡¡ Las barras de pan del día de ayer tienen un descuento del 60% !!!')
print(f'Una barra de pan de ayer te costará {pan_viejo} $')
compra_usuario = float(input('Calcula el precio final despues de comprar varias barras de pan de ayer, INGRESA CANTIDAD DE PANES => '))
calculo_usuario = pan_viejo * compra_usuario
print(f'Tu Precio final será de {calculo_usuario}')
print('GRACIAS POR TU COMPRA')