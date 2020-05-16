# exercise059
from time import sleep
n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))
menu = 0
while menu != 5:
    menu = int(input("""Enter your menu option:
    [1] - Addition
    [2] - Subtraction
    [3] - Highest
    [4] - New Numbers
    [5] - Exit
    """))
    if menu == 1:
        print(f'Option 1: n1 {n1} + {n2} n2 = {n1 + n2}')
    if menu == 2:
        print(f'Option 2: n1 {n1} X {n2} n2 = {n1 * n2}')
    if menu == 3:
        if n1 > n2:
            print(n1)
        if n1 < n2:
            print(n2)
        else:
            print('You have entered 2 equal numbers.')
    if menu == 4:
        print('Option 4: New numbers...')
        n1 = int(input('Enter a new number: '))
        n2 = int(input('Enter another new number: '))
    else:
        print('Invalid option, try again...')
    sleep(2)
print(f'Option 5: Exit...')
