# exercise100
from random import randint
from time import sleep
def sort_list(create_list):
    print('Sorting 5 values: ', end='')
    for count in range(0, 5):
        num = randint(1, 10)
        create_list.append(num)
        print(f'{num} ', end='')
        sleep(0.3)
    print('DONE!')


def sumEven(create_list):
    sum = 0
    for value in create_list:
        if value % 2 == 0:
            sum += value
    print(f'Sum values of the list {create_list} = {sum}.')


# Main Program

numbers = []
sort_list(numbers)
sumEven(numbers)