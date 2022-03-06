from Users import *
from Constants import *
from Functions import *
import pprint

if __name__ == '__main__':

    username_in = input('Please enter your username: ')
    password_in = input('Please enter your password: ')

    if username_in in USERS and (PASSWORDS[USERS.index(username_in)] == password_in):
        print(ODDELOVAC)
        print('Welcome to the app, ', username_in, '!\nWe have 3 texts to be analyzed.')
        print(ODDELOVAC)
        cislo_in = (input('Enter a number btw. 1 and 3 to select:'))
        if cislo_in.isdigit() and 1 <= int(cislo_in) < 3:
            print('There are ', pocet_slov, ' words in the selected text.')
            print('There are ', pocet_slova_title, ' titlecase words.')
            print('There are ', pocet_slova_upper, ' uppercase words.')
            print('There are ', pocet_slova_lower, ' lowercase words.')
            print('There are ', pocet_slova_cisla, ' numeric strings.')
            print('The sum of all the numbers ', suma_celkem, '.')
            print(ODDELOVAC)
            print("{:<5}{:<20}{:<4}".format('LEN |', ' OCCURENCES ', ' | NR.'))
            print(ODDELOVAC)
            for k, v in slovnik.items():
                pocet = '*' *  k
                print(f'{i:3} | {pocet:19} | {k:4d}')
                i = i + 1
        else:
            print('The choice ', cislo_in, 'is not in the offer. Terminating the program...')
    else:
        print('Unregistered user, terminating the program...')


