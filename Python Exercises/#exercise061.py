# exercise061
a1 = int(input('Enter the first term in the Arithmetic Progression: '))
d = int(input('Enter the common difference between terms: '))
count = 1
t = a1
while count != 10:
    print(f'{t}', end='->')
    t += d
    count += 1
print('THE END')
