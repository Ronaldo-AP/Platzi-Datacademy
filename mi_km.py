import os
import platform
import time


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')



def welcome():

    line = '+' + '-'*98 + '+\n'
    title = '|' + 'CONVERSOR MILLAS - KILOMETROS'.center(98,' ') + '|\n'
    welcome = line + title + line + '\n'

    while True:
        clear_screen()
        print(welcome)

        question = '¿Qué conversión desea realizar?\n'
        conversion = '1. km --> mi \n2. mi --> km\n'
        
        try:
            option = int(input(question + conversion))
            if option == 1 or option == 2:
                break
            else: 
                print('Introduce un opción correcta')
                time.sleep(1)
                continue
        except ValueError:
            print('Introduce una opción correcta')
            time.sleep(1)
            continue
    
    return option



def mi_to_km():
 
    while True:
        try:
            out = '\nIntroduce las millas a convertir: '
            mi = float(input(out))
            break
        except ValueError:
            print('Introduce un valor válido')
            continue
    
    km = round(mi*1.609344, 2)
    converted = f'{mi} mi --> {km} km'
    print(converted)



def km_to_mi():
     
    while True:
        try:
            out = '\nIntroduce los kilómetros a convertir: '
            km = float(input(out))
            break
        except ValueError:
            print('Introduce un valor válido')
            continue
    
    mi = round(km/1.609344, 2)
    converted = f'{km} km --> {mi} mi'
    print(converted)



def main():

    option = welcome()
    if option == 1:
        km_to_mi()
    elif option == 2:
        mi_to_km()

        

if __name__ == '__main__':
    main()