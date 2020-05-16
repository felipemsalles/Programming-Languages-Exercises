# exercise063
num = int(input('Enter a number: '))
t1 = 0
t2 = 1
print(f'{t1}->{t2}', end='')
counter = 3
while counter <= num:
    t3 = t1 + t2
    print(f'->{t3}', end='')
    counter += 1
    t1 = t2
    t2 = t3
print('->THE END')