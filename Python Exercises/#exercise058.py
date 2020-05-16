# exercise058
from random import randint
print('The computer will choose a number between 0-10(inclusive), try to guess!')
computer = randint(0, 10)
correct = False
count = 0
while not correct:
    attempt = int(input('Enter a number between 0-10(inclusive): '))
while not correct:
    attempt = int(input('Enter a number between 0-10(inclusive): '))
    if attempt > computer:
        print('LESS...')
    elif attempt == computer:
        correct = True
    else:
        print('MORE...')
    count += 1
print(f'Congratulations, you chose the correct number {computer} in {count} attempts!')