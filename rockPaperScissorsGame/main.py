import random

options = ['rock','paper','scissors']
pc = random.choice(options)
user = None

while True:
    options = ['rock','paper','scissors']

    pc = random.choice(options)
    user = None

    def resultado(pc, user):
        print('O usuário jogou: ' + user)
        print('O pc jogou: ' + pc)

    while user not in options:
        user = input('rock, paper or scissors?').lower()

    if pc == user:
        resultado(pc,user)
    elif user == 'rock':
        if pc == 'paper':
            resultado(pc,user)
            print('PC wins')
        else:
            resultado(pc,user)
            print('USER wins')
    elif user == 'paper':
        if pc == 'scissors':
            resultado(pc, user)
            print('PC wins')
        else:
            resultado(pc, user)
            print('USER wins')
    elif user == 'scissors':
        if pc == 'rock':
            resultado(pc, user)
            print('PC wins')
        else:
            resultado(pc, user)
            print('USER wins')

    play_again = input("Play again? yes/no: ").lower()
    if play_again != 'yes':
        print('I hope u enjoyed the game!')
        break
