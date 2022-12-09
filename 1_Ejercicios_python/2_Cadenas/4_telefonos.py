

'''
EJERCICIO 4

Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''

print('TEN PRESENTE ESTE FORMATO DE GUI => +34-913724710-56 ')
print('Donde +34 = Es el codigo de tu país ')
print('Donde -913724710- = Es tu numero ')
print('Donde -56 Es la extensión')

numero = input('Ingresa tu numero Siguiendo el formato => ')
print(numero[4:12])