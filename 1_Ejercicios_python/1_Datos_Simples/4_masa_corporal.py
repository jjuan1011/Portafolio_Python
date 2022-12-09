

'''
ejercicio 7

Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
'''

peso = float(input('Ingresa tu peso en kilogramos => '))

print('======================================')
print('Para tu estatura en centimetros puedes usar nuestra guia de talla\n')
print(' si tu estatura es 1 metro 55 centimetro = 1.55\n si tu estatura es 1 metro 65 centimetros = 1.65\n si tu estatura es 1 metro 70 centimetros = 1.70')
print('======================================')
estatura = float(input('Ingresa tu altura en metros ==>> '))

imc = peso / estatura**2

print(f'Tu índice de masa corporal es {imc} donde {imc} es el índice de masa corporal calculado redondeado con dos decimales.')

