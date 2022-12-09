

'''
EJERCICIO 10 

Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 10 años debe pagar 25000, si tiene entre 10 y 15 años debe pagar 30000 y si es mayor de 16 años, 50000.
'''


class Juegos():
    def __init__(self):
        print('============================== BUINVENIDOS A SALITRE MÁGICO ===================================')
        self.edad = int(input('Ingresa tu edad para conocer el precio de tu entrada y las atracciones que puedes usar => '))

    def atraciones_disponibles(self):
        print('========================== BUENVENIDO A JUEGOS SALITRE MÁGICO ================================')
        self.atracciones = {
                "atracciones_infantiles" : {
                'atracciones': ['Baby Zone', 'Jumping Start','Laberinto','Marine Bay','Mini Rueda','Zamba Balloon', 'Speed Way', 'Trency', 'Mini Autos'],
                'Pasaporte Nitro': ['Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica'],
                'Pasaporte Kids': ['Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica'],
                'Estatura Minima': [90,80,80,90,90,90,90,105],
                'Estatura Maxima': [100,150,130,150,150,150,150,150,150]
        },
                "atracciones_familiares" : {
                'atracciones': ['Avion 727', 'Monstruos Marinos','Juegos Destreza','Crazy Plane','Gusano Loco','Mini Jet', 'Carrusel', 'Palacio de Cristal', 'Rueda Capital 360','Sillas Voladores', 'Convoy', 'Splash'],
                'Pasaporte Nitro': ['Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica'],
                'Pasaporte Kids': ['Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica'],
                'Estatura Minima': [90,80,80,90,90,90,90,105],
                'Estatura Maxima': [100,150,130,150,150,150,150,150,150]
        },

                "atracciones_alto_impacto" : {
                'atracciones': ['Apocalipsis', 'Barco Pirata','Centrox','Doble Loop','Montaña Rusa','Castillo Terror', 'Super Shot', 'Pista Karts', 'Carros Chocones'],
                'Pasaporte Nitro': ['Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica','Aplica'],
                'Pasaporte Kids': ['No Aplica','No Aplica','No Aplica','No Aplica','No Aplica','No Aplica','No Aplica','No Aplica','No Aplica'],
                'Estatura Minima': [90,80,80,90,90,90,90,105],
                'Estatura Maxima': [100,150,130,150,150,150,150,150,150]
        }
        }
        print('=============================================================================================')
        for i in self.atracciones.items():
            print(i)

    def precio(self):
        if self.edad <= 4:
            print('Tu ingreso es gratis mocoso')
        elif self.edad > 4 and self.edad <= 10:
            print('Debes pagar 25.000 pesos')
        elif self.edad > 10 and self.edad <= 15:
            print('Debes pagar 30.000 Pesos')
        elif self.edad > 16:
            print('Debes pagar 50.000 Pesos')
        else:
            print('Ingresa un opción válida putito')

   
    


jugador = Juegos()
print(jugador.atraciones_disponibles())
print(jugador.precio())

