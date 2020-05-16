# exercise028
from random import randint
print('The computer will chose a number between 0 - 5 (inclusive), try to guess!')
pc = randint(0, 5)
attempt = int(input('Enter a number to guess the secret number: '))
if attempt == pc:
    print(f'You won, the number was: {pc}!')
else:
    print(f'You lost, the secret number = {pc} was different from your number.')

















