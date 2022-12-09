
'''
EJERCICIO 7

Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''

email = str(input('Ingresa tu correo electronico para convertirlo por ti => '))

print(email[:email.find('@')] + '@ceu.es')

# Una herramiento muy increíble

# Con ella podemos decirle que busque cierto grupo o tipo de caracteres y que corte ahí y lo que sigue lo reemplace por lo que nosotros queramos, por ejemplo acá el numero de unatarjeta en cuanto detecta los numeros  llave de una tarjeta visa imprime el mensaje diciendo que efectivamente es una visa

prueba = input('=> ')
print(prueba[:prueba.find('1000')] + 'Esta es una tarjeta Visa')