

'''
BET PLAY

Crear un programa de apuestas futboleras en la que Programa agarre dos equipos de una lista y el usuario lance su apuesta hacia dichos equipos y que se de un resultado de forma aleatoria tambien, despues segun el resultado mirar si el usuario ganó o perdió y cuando ganó, esto las veces que sea necesario hasta que el usuario decida salir del programa
'''
import random

class Bet_play():
    def __init__(self):
        self.teams = ["Argentina", "Alemania", "Holanda", "Francia",                        
        "Colombia","Inglaterra", "Portugal", "Brasil", "España", "Italia", "Suecia", "Uruguay", "Croacia", "Chile"]
        self.score = [1,2,3,4,5,6,7,8,9,10]
        self.request = ''
    
    def bet_now(self):
        while self.request != 2:
            
            print('========================= APUESTA AHORA =============================')
            self.computer_election_1 = random.choice(self.teams)
            self.computer_election_2 = random.choice(self.teams)
            print(f"====== {self.computer_election_1} VS {self.computer_election_2} ======")
            self.usser_bet = input('Ingresa el Nombre del equipo en el cual confías tu dinero =>>> ').capitalize() #´Primera letra Mayuscula
            self.cant_bet = int(input('Ingresa la cantidad que deseas apostar => '))

            # for self.usser_bet in self.teams:
            #     if self.usser_bet in self.teams:
            #         print(f'Tu elección ♥♥♥ => {self.usser_bet}')
# Probabilidades de ganancia o perdida => 
            self.score_election_1 = random.choice(self.score)
            self.score_election_2 = random.choice(self.score)
            print({self.computer_election_1},'=>',{self.score_election_1}, 
            {self.computer_election_2} , '=>' , {self.score_election_2})

            if self.score_election_1 == self.score_election_2 :
                print('¡¡¡ EMPATE !!!  Pierdes la mitad de tu dinero puto ;(')
            
            if self.usser_bet == self.computer_election_1:
                if self.score_election_1 > self.score_election_2:
                    print('Gana', (self.computer_election_1), 'Ganaste', (self.cant_bet * 10), 'Pesos :)')
                else:
                     print('Gana', (self.computer_election_2), 'Perdiste hijo de re mil putas ;(')
            if self.usser_bet == self.computer_election_2:
                if self.score_election_1 < self.score_election_2:
                    print('Gana', (self.computer_election_1), 'Ganaste', (self.cant_bet * 10), 'Pesos :)')
                else:
                     print('Gana', (self.computer_election_1), 'Perdiste hijo de re mil putas ;(')
                
            self.request = int(input('Si desea hacer otra apuesta ingrese => 1 si desea salir ingrese => 2     ¿QUÉ DESEAS HACER? =>>> '))       

apuesta = Bet_play()
apuesta.bet_now()
