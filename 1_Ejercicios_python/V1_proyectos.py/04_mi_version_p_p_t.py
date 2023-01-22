

'''
Mi versión de piedra papel o tijera
'''
import random
class Videogame():
    def __init__(self):
        self.options = ['piedra', 'papel', 'tijera']
        self.computer_option = random.choice(self.options)
        self.computer_score = 0
        self.user_score = 0
        
    
    def game(self):
        while self.computer_score < 3 or self.user_score < 3:
            self.user_option = str(input('PIEDRA, PAPEL O TIJERA, Ingrese su opción =>>> ')).lower()
            if self.user_option == self.computer_option:
                print('¡¡¡ Empate !!!')
                self.computer_score += 1
                self.user_score += 1
                self.global_score = print(f'User => {self.user_score}, Computer => {self.computer_score}')
            elif self.user_option == 'piedra':
                if self.computer_option == 'papel':
                    print('¡ Papel gana a piedra !')
                    print(' Computer Wins !!!')
                    self.computer_score += 1
                    self.global_score = print(f'User => {self.user_score}, Computer => {self.computer_score}')
                elif self.computer_option == 'tijera':
                    print('¡ Piedra gana a tijera !')
                    print(' User Wins !!!')
                    self.user_score += 1
                    self.global_score = print(f'User => {self.user_score}, Computer => {self.computer_score}')
            elif self.user_option == 'papel':
                if self.computer_option == 'piedra':
                    print('¡ Papel gana a piedra !')
                    print(' User Wins !!!')
                    self.user_score += 1
                    self.global_score = print(f'User => {self.user_score}, Computer => {self.computer_score}')
                elif self.computer_option == 'tijera':
                    print('¡ Tijera gana a papel !')
                    print(' Computer Wins !!!')
                    self.computer_score += 1
                    self.global_score = print(f'User => {self.user_score}, Computer => {self.computer_score}')
            elif self.user_option == 'tijera':
                if self.computer_option == 'piedra':
                    print('¡ Piedra gana a tijera !')
                    print(' Computer Wins !!!')
                    self.computer_score += 1
                    self.global_score = print(f'User => {self.user_score}, Computer => {self.computer_score}')
                elif self.computer_option == 'papel':
                    print('¡ Tijera gana a papel !')
                    print(' User Wins !!!')
                    self.user_score += 1
                    self.global_score = print(f'User => {self.user_score}, Computer => {self.computer_score}')

game_run = Videogame()
game_run.game()   

  

videogame = Videogame()
