# exercise068
print('EVEN OR ODD!')
from random import randint
wins = 0
while True:
    num = int(input('Enter a number: '))
    computer = randint(0, 10)
    tot = num + computer
    option = ' '
    while option not in 'EO':
        option = str(input('Even or Odd ? [E/O]')).strip().upper()[0]
    print(f'User Number = {num} | Computer Number = {computer}. Total = {tot}!')
    if option == 'E':
        if tot % 2 == 0:
            print(f'EVEN, YOU WON!')
            wins += 1
        else:
            print('YOU LOST.')
            break
    elif option == 'O':
        if tot % 2 == 1:
            print(f'ODD, YOU WON!')
            wins += 1
        else:
            print('YOU LOST.')
            break
    print('Lets try again...')
print(f'GAME OVER! Total of consecutive wins = {wins}.')