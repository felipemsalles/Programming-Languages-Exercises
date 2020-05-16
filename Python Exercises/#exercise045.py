# exercise045
from time import sleep
import random
print("""
[0] - Rock
[1] - Paper
[2] - Scissors
""")
user = int(input('Enter an option to challenge the computer: '))
computer = random.randint(0, 2)
print("ROCK")
sleep(1)
print("PAPER")
sleep(1)
print("SCISOORS!!!")

if computer == 0:
    print(f'COMPUTER - ROCK!')
    if user == 0:
        print(f'TIE!')
    elif user == 1:
        print(f'YOU WON!')
    elif user == 2:
        print(f'YOU LOST!')
    else:
        print('INVALID OPERATION!')
elif computer == 1:
    print(f'COMPUTER - PAPER')
    if user == 0:
        print(f'YOU LOST!')
    elif user == 1:
        print(f'TIE!')
    elif user == 2:
        print(f'YOU WON!')
    else:
        print('INVALID OPERATION!')
elif computer == 2:
    print(f'COMPUTER - SCISSORS')
    if user == 2:
        print('TIE!')
    elif user == 0:
        print('YOU WON!')
    elif user == 1:
        print('YOU LOST!')
    else:
        print('INVALID OPERATION!')
else:
    print('INVALID OPERATION!')