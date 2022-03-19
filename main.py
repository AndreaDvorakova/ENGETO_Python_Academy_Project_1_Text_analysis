from Users import *
from Constants import *
from Functions import *

if __name__ == '__main__':

    username_in = input('Please enter your username: ')
    password_in = input('Please enter your password: ')

    if username_in in USERS and (PASSWORDS[USERS.index(username_in)] == password_in):
        print(ODDELOVAC)
        print('Welcome to the app, ', username_in, '!\nWe have 3 texts to be analyzed.')
        print(ODDELOVAC)
        volba = input('Enter a number btw. 1 and 3 to select: ')
        cislo_in = int(volba) - 1
        if volba.isdigit() and 1 <= int(volba) <= 3:
            statistika_textu(cislo_in)
            statistika_slov_graficky()
            print(ODDELOVAC)
            print("{:<5}{:<20}{:<4}".format('LEN |', ' OCCURENCES ', ' | NR.'))
            print(ODDELOVAC)
            for k, v in slovnik.items():
                pocet = '*' *  k
                print(f'{i:3} | {pocet:19} | {k:2d}')
                i = i + 1
        else:
            print('The choice', volba, 'is not in the offer. Terminating the program...')
    else:
        print('Unregistered user, terminating the program...')


