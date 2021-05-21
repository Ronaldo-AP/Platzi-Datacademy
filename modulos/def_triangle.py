import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def welcome():
    clear_screen()
    print('+' + '-' * 98 + '+')
    print('|' + 'CALCULADORA DE TRIANGULOS'.center(98, ' ') + '|')
    print('+' + '-' * 98 + '+')
    print('| Hola bienvenido a su calculadora de área de triangulos'.ljust(99, ' ') + '|')
    print('| Para poder ayudarle necesitaré de algunos datos '.ljust(99, ' ') + '|')
    print('+' + '-' * 98 + '+')
    print()


def init_arguments():
    b = .0
    h = .0
    while True:
        try:    
            b = float(input('Base del Triángulo: '))
            h = float(input('Altura del Triángulo: '))
            break
        except ValueError:
            continue

    while True:
        if b <= .0 or h <= .0:
            print('Introduzca valores no nulos positivos')
        else:
            break

    return b, h


def init_sides(triangle):
    side_a = .0
    side_c = .0

    print('+' + '-' * 98 + '+')
    print('| Se necesita conocer los otros dos lados'.ljust(99, ' ') + '|')
    print('+' + '-' * 98 + '+')

    while True:
        try:    
            side_a = float(input('Lado A del Triángulo: '))
            side_c = float(input('Lado B del Triángulo: '))
            if side_a < triangle.height or side_c < triangle.height:
                raise ValueError('¿Es el mismo triángulo? Los lados no pueden ser menores que la altura')
            else: break
        except ValueError:
            continue

    while True:
        if side_a <= .0 or side_c <= .0:
            print('Introduzca valores no nulos y positivos')
        else:
            break

    return side_a, side_c

def continue_question():
    while True:
        out = '¿Desea continuar con el cálculo de mas propiedades? [y/n]\n'
        ans = str(input(out))
        if ans == 'y' or ans == 'n': break
    if ans == 'n': exit()


        
    


    




