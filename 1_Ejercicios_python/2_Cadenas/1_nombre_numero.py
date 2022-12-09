

'''
EJERCICIO 1 

Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''
nombre = str(input('Ingresa tu bello nombre afeminado Hijo de Perra => '))
numero = int(input('Ingresa un numero amigue => '))

# La logica es concatenar el nombre con el salto de lines y eso multiplicarlo por la cantidad puesta por el usuario
print((nombre + "\n") * numero)