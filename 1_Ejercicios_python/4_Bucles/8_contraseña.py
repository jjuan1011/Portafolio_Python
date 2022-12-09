

'''
Ejercicio 9

Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

class Contraseña():
    def __init__(self):
        self.contraseña = 'contraseña'
        self.credenciales = ''
    
    def rectificador(self):
        while self.credenciales != self.contraseña:
            self.credenciales = str(input('\n Ingrese su contraseña => '))
            print('\n \n INGRESA BIEN LA CONTRASEÑA PUTO')
        print(' \n \n => Contraseña Correcta => \n ========== INGRESAS DE FORMA ÉXITOSA AL CANAL ==========\n')
            
            
contraseña = Contraseña()
contraseña.rectificador()

