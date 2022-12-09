

'''
Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
'''

class Abecedario():
    def __init__(self):
        self._abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

    def modificando(self):
        for i in range(len(self._abc), 1, -1):
            if i % 3 == 0:
                self._abc.pop(i-1)
        print(self._abc)


abcdario_modificado = Abecedario()
abcdario_modificado.modificando()

