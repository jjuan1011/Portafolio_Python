

'''
EJERCICIO 10

Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
'''

cesta = str(input('Ingrese los roductos de su cesta, separados por una coma => '))

# Utiliamos el replace para REEMPLAZAR la coma por un salto de linea
print(cesta.replace(',', '\n'))

