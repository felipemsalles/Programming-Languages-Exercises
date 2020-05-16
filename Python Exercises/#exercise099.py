# exercise099
from time import sleep
def higher(*num):
    count = higher = 0
    print('-=' * 30)
    print('\nAnalyzing the values...')
    for value in num:
        print(f'{value} ', end='')
        sleep(0.3)
        if count == 0:
            higher = value
        else:
            if value > higher:
                higher = value
        count += 1
    print(f'Total of Values: {count}.')
    print(f'Higher value: {higher}.')


# Main Program
higher(4, 5, 6, 7, 8)
higher(0, 2)
higher(5, 20)
higher()