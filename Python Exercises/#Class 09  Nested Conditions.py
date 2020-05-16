# Simple Condition
name = str(input('What is your name ? '))
if name == 'Jack':
    print('Beatiful name!')
print(f'Have a good day {name}!')

# Composed Condition
name = str(input('What is your name ? '))
if name == 'Jack':
    print('Beatiful name!')
elif name == 'Charlie' or name == 'Robert' or name == 'Cris':
    print('Your name is very popular in United States.')
elif name in 'Eliza Julia Ellie Emma':
    print('Beatiful female name!')
else:
    print('Your name is very common.')
print(f'Have a good day {name}!')
