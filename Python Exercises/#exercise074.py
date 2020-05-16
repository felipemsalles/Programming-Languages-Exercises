# exercise074
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))  # random tuple
print(f'Tuple: {n}')
s = (sorted(n))
print(f'Lower: {s[0]}')
print(f'Higher: {s[4]}')
print('=' * 30)


# Another Solution
numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Sorted values: ', end='')
for i in numbers:
    print(f'{i} ', end='')
print(f'\nLower value: {min(numbers)}')
print(f'Higher value: {max(numbers)}')