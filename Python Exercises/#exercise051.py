# exercise051
a1 = int(input('First term of the Arithmetic Progression: '))
d = int(input('Enter the common different between terms: '))
for c in range(a1, a1+(10 * d), d):
    print(f'{c}--', end='-> ')
print('THE END')



