

'''
Ejercicio 13

Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
'''

class Eco():
    def __init__(self):
        self.ingrese = ''
        self.salir = ''
        
    
    def programa(self):
        while self.salir != 'x':
            self.ingrese = input('Ingrese lo que le salga del culo => ')
            self.ingrese = self.ingrese.lower()
            print(self.ingrese)
            self.salir = input('Para salir ingrese => x, Par continuar Ingrese => y \n INGRESE ================> ')
        

ecos = Eco()
ecos.programa()


# Otra forma de hacerlo
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)
         
