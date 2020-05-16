"""for c in range (1, 10):
    print(c)
print('THE END')"""
print('-' * 30)


c = 1
while c < 10:
    print(c)
    c += 1
print('THE END!')
print('-' * 30)

"""for c in range(1, 5):
    n = int(input('Enter a number: '))
print('THE END!')"""""


n = 1
while n != 0:
    n = int(input('Enter a number:'))
print('THE END!')
print('-' * 30)


answer = 'Y'  # Y = Yes | N = No
while answer == 'Y':
    n = int(input('Enter a number: '))
    answer = str(input('Do you want to continue ? [Y/N]')).upper()
print('THE END!')
print('-' * 30)


n = 1
even = 0
odd = 0
while n != 0:
    n = int(input('Enter a number: '))
    if n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
print(f'Even numbers = {even}; Odd numbers =  {odd}.')
