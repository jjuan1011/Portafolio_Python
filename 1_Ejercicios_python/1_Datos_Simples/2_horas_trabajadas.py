
'''
EJERCICIO 5

Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
'''

horas_trabajadas = float(input('Escribe el numero de horas que trabajaste esta semana =>  '))
valor_hora_trabajo = float(input('Ingresa la cifra exacta del valor de tu hora dada por tu supervisor => '))

paga_final = horas_trabajadas * valor_hora_trabajo
print(paga_final)


# IMPORTANTE !!!1

# Cuando le pidamos al usuario que ingrese un numero debemos ponerle al input un type float o int para que el programa NO tome le numero ingresado como una string