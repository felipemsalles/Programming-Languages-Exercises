# exercise020

from random import shuffle
name1 = str(input('Enter the name of the first student: '))
name2 = str(input('Enter the name of the second student: '))
name3 = str(input('Enter the name of the third student: '))
name4 = str(input('Enter the name of the fourth student: '))
sequence = [name1, name2, name3, name4]
shuffle(sequence)
print(f'The sequence of the presentation will be: {sequence}')
