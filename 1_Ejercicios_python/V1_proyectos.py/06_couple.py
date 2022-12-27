

'''
PROYECTO

Juego interctivo:

- con condcicionales
- opciones de una tupla
- Iteraciones + condicionales
- Metodos
- funciones
- Random
- Operaciones
'''
import random

class Love():
    def __init__(self):
        self.points = [1,2,3,4,5,6,7,8,9,10]
        self.couple_men = []
        self.couple_woman = []
        self.couple_all = []
        self.request = ""
    
    def proof(self):
        while self.request != 2:
            self.name = str(input('Ingresa tu Nombre =>>> '))
            print(f'Hola {self.name} Bienvenido/a, Empecemos .............')
            print('========================== OPCIONES ============================')
            print('Para buscar pareja ingrese => A')
            print('Para Mirar qué tan gay es ingrese  => B')
            print('Para ver tu destino en pareja ingresa C ')
            self.option = str(input('Ingresa la letra según lo que desees hacer => ')).lower()
            
            if self.option == 'a':
                print('===============================================================')
                self.sex = input('Si te gustan los hombres ingresa => H\n Si te gustan las mujeres ingresa => M\n Si comes de todo ingresa => T.\n  INGRESA AQUÍ >>> ').lower()
                
                if self.sex == 'h':
                    print('===============================================================')
                    print('Veo que te gustán los chicos, así que has una lista de los chicos que te gustan y el sistema eligirá por ti ♥♥♥')
                    for i in range(5):
                        print('===============================================================')
                        self.couple_men.append(str(input('Ingresa tus mejores 5 opcines => ')))
                        print(f'Opción = {i}')
                    self.ideal_pair = random.choice(self.couple_men)
                    print(f'Tu pareja ideal es => {self.ideal_pair}')
                elif self.sex == 'm':
                    print('===============================================================')
                    print('Veo que te gustán las chicas, así que has una lista de los chicas que te gustan y el sistema eligirá por ti ♥♥♥')
                    for i in range(5):
                        self.couple_woman.append(str(input('Ingresa tus mejores 5 opcines => ')))
                        print(f'Opción = {i}')
                    self.ideal_pair = random.choice(self.couple_woman)
                    print('===============================================================')
                    print(f'Tu pareja ideal es => {self.ideal_pair}')
                elif self.sex == 't':
                    print('===============================================================')
                    print('Veo que le tiras a todo, así que has una lista de los personajes que te gustan y el sistema eligirá por ti ♥♥♥')
                    for i in range(5):
                        self.couple_all.append(str(input('Ingresa tus mejores 5 opcines => ')))
                        print(f'Opción = {i}')
                    self.ideal_pair = random.choice(self.couple_all)
                    print('===============================================================')
                    print(f'Tu pareja ideal es => {self.ideal_pair}')
            
            if self.option == 'b':
                print('===============================================================')
                self.question = ['Color favorito', 'Marca de ropa que más usas','Preferencia, Dinero o Amor', ]
                for i in self.question:
                    self.rta = str(input(f'¿ Cuál es tu {i} => '))
                    print(self.rta)
                self.gay = random.choice(self.points)
                print('===============================================================')
                print(f'Eres {self.gay} % GAY ;) ')
            
            if self.option == 'c':
                print('===============================================================')
                self.couple_destiny = ['Vas a Morir solo y pajero', 'Tendrás 45 años de matrimonio', 'Te casarás y te divorsiarás en 1 año', 'No tienes futuro en pareja, moriras el otro año ;)', 'Tendrás muchas perras :D']
                self.destiny = random.choice(self.couple_destiny)
                print('===============================================================')
                print(f' Añañin dice que tu destino es => {self.destiny}')
                print('===============================================================')
            
            self.request = int(input('Para volver a jugar ingresa => 1 \n Para salir ingresa => 2\n   >>>>>>  >>>>>>> INGRESA TU OPCIÓN >>>  '))
            

program = Love()
program.proof()