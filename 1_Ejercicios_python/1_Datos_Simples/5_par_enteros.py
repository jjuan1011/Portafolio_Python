
'''
EJERCICIO 8

Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''
entero_1 = int(input('Ingrese el primer numero entero => '))
entero_2 = int(input('Ingrese el segundo numero entero => '))

cociente = entero_1 / entero_2
residuo = entero_1 % entero_2

print(f'El cocinte o resultado de dividir entre dos es => {cociente}')
print(f'El resto de la division es => {residuo} ')