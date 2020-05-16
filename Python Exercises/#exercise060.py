# exercise060

# First Solution
from math import factorial
num = int(input('Enter a number: '))
fac = factorial(num)
print(fac)

# Second Solution
num = int(input('Enter a number: '))
c = num
f = 1
while c > 0:
    print(f'{c}', end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(f'{f}')