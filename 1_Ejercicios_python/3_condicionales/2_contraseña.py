
'''
EJERCICIO 2

Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

class Contraseña():
    def __init__(self):
        self.nombre_usuario = str(input('Ingresa tu Usuario => '))
        self.contraseña_usuario = str(input('Ingresa tu contraseña => '))
        self.contraseña_correcta = '1001'
        self.nombre_usuario_correcto = 'Nemesiq'

    def prueba_nombre_usuario(self):
        if self.nombre_usuario == self.nombre_usuario_correcto:
            print('Usuario correcto')
        else:
            print('Usuario incorrecto')
    
    def prueba_contraseña(self):
        if self.contraseña_usuario == self.contraseña_correcta:
            print('La contraseña es correcta, INGRESAS CON EXITO')
        else:
            print('La contraseña es incorrecta, ¿ACASO INTENTAS HACKEAR LA CUENTA?')

credenciales = Contraseña()
print(credenciales.prueba_nombre_usuario())
print(credenciales.prueba_contraseña())
