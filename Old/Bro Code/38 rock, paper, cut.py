import random
cho = {'rock': 'paper', 'paper': 'cut', 'cut': 'rock'}
choices = tuple(cho.keys())
while True:
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input('Make a choice - rock, paper, cut: ')
    print('Computer chose:', computer)
    print('REZ: ', end='')
    if player == computer:
        print('nothing at all')
    elif cho[player] == computer:
        print('you loose.')
    else:
        print('YOU WIN!')
    print('----------------------------------------------------------------')
    if input('Play again? ') != 'yes':
        break
print('\nBye!')
