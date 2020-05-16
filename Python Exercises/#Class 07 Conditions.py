name = str(input('What is your name ? '))
if name == 'Jack':
    print('Beatiful name!')
else:
    print('Your name is common to hear!')
print(f'Bom dia, {name}!')
# works in 2 different types of conditions
n1 = float(input('Enter the first grade: '))
n2 = float(input('Enter the second grade: '))
average = (n1 + n2) / 2
print(f'Your average is: {average:.1f}')
if average >= 6.0:
    print('Great average, congratulations!')
else:
    print('Your average is not good, you should study more!')
# print('Congratulations' if avarage >= 6.0 else 'Study more!' simple condition