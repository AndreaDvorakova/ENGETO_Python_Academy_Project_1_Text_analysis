from Users import *
from Constants import *

if __name__ == '__main__':

    username_in = input('Please enter your username: ')
    password_in = input('Please enter your password: ')

    if username_in in USERS and (PASSWORDS[USERS.index(username_in)] == password_in):
        print('nabidka')
    else:
        print('nic')


