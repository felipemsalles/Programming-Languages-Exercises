# exercise052
n = int(input('Enter a number:'))
count = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        count += 1
    else:
        print('\033[31m', end='')
print(f'{n} was divisible  {count} times.')
if count == 2:
    print('So, IS A PRIME NUMBER!')
else:
    print('So, IS NOT A PRIME NUMBER.')