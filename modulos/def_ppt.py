import os
import platform
import random
import time


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')



def welcome():
    clear_screen()
    print('+' + '-' * 98 + '+')
    print('|' + 'PIEDRA PAPEL O TIJERA'.center(98, ' ') + '|')
    print('+' + '-' * 98 + '+')
    print('| Hola bienvenido a su juego favorito'.ljust(99, ' ') + '|')
    print('+' + '-' * 98 + '+')
    print()



def choose_mode():
    while True:
        out = '¿Desea jugar con la maquina? [y/n]\n'
        ans = str(input(out))
        if ans == 'y' or ans == 'n': break
    if ans == 'y': mode = True
    else: mode = False
    return mode



def win_player(game):

    if game[1]['option'] == game[2]['option']:
        print('EMPATE')

    elif game[1]['option'] == 'piedra':

        if game[2]['option'] == 'papel': 
            print(f'Ronda para {game[2]["player"]}')
            game[2]['points'] += 1

        elif game[2]['option'] == 'tijera': 
            print(f'Ronda para {game[1]["player"]}')
            game[1]['points'] += 1

    elif game[1]['option'] == 'papel':

        if game[2]['option'] == 'piedra': 
            print(f'Ronda para {game[1]["player"]}')
            game[1]['points'] += 1

        elif game[2]['option'] == 'tijera': 
            print(f'Ronda para {game[2]["player"]}')
            game[2]['points'] += 1

    elif game[1]['option'] == 'tijera':

        if game[2]['option'] == 'papel': 
            print(f'Ronda para {game[1]["player"]}')
            game[1]['points'] += 1

        elif game[2]['option'] == 'piedra': 
            print(f'Ronda para {game[2]["player"]}')
            game[2]['points'] += 1
    
    time.sleep(1.5)
    
    return game
    


def print_winner(out, rounds, points):
    clear_screen()
    print('+' + '-' * 98 + '+')
    print('|' + f'EL SUPER GANADOR ES: {out} EN {rounds} RONDAS CON {points} PUNTOS'.center(98, ' ') + '|')
    print('+' + '-' * 98 + '+')



def IA_game():

    rounds = 0
    options = {1:'piedra', 2:'papel', 3:'tijera'}
    game = {
        1 : {
            'player' : 'IA',
            'points' : 0,
            'option' : None
        },
        2 : {
            'player' : 'Player',
            'points' : 0,
            'option' : None
        }
    }

    while True:
        rounds += 1

        while True:
            try:
                clear_screen()
                out = f'\nEscoge tu jugada: (Ronda {rounds})\n1. Piedra\n2. Papel\n3. Tijera\n\n'
                i = int(input(out))
                if i == 1 or i == 2 or i == 3:
                    pers = options[i]
                    break
                else: 
                    print('Introduce una opción correcta')
                    time.sleep(1)
                    continue
            except ValueError:
                print('Introduce una opción correcta')
                time.sleep(1)
                continue
        
        game[1]['option'] = options[random.randint(1,3)]
        game[2]['option'] = pers 
        
        game = win_player(game)

        if game[1]['points'] >= 2 or ( game[1]['points'] == 1 and game[2]['points'] == 0 and rounds >= 3 ):
            print_winner(game[1]['player'], rounds, game[1]['points'])
            break
        elif game[2]['points'] >= 2 or ( game[2]['points'] == 1 and game[1]['points'] == 0 and rounds >= 3 ):
            print_winner(game[2]['player'], rounds, game[2]['points'])
            break
        else: continue








                    
        
            




