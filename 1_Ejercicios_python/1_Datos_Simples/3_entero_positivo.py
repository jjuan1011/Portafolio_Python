
'''
EJERCICIO 6

Escribir un programa que lea un entero positivo, n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
'''

n = int(input('Ingresa un numero ENTERO POSTIVO del 1 al 100 => '))

operacion_con_enteros = n * (n + 1)/2

print(operacion_con_enteros) 

# Si el usuario ingresa 5 el resultado será 15.0 ya que se suman todos los números del 1 al 5

# 1 + 2 + 3 + 4 + 5 = 15