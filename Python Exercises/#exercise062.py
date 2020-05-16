# exercise062
first_term = int(input('Enter the first term in the sequence: '))
d = int(input('Enter the common difference between terms: '))
count = 1
term = first_term
total = 0
more = 10
while more != 0:
    total += more
    while count <= total:
        print(f'{term}', end='->')
        term += d
        count += 1
    print('PAUSING...')
    more = int(input('Enter more term numbers to print: '))
print(f'THE END - Total of terms = {total}.')