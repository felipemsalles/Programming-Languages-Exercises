n1 = int(input('Enter a number:'))
n2 = int(input('Enter another number:'))
sum = n1 + n2
print(f'The sum of {n1} + {n2} is {sum}')

# Challenge 3
n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))
sum = n1 + n2
print(f'The sum of {n1} and {n2} is: {sum}')

# Challenge 4
n = input('Enter something: ')
print(type(n))  # print the type of n.
print(f'{n} Is Numeric ?:', n.isnumeric())
print(f'{n} Is Alpha ?:', n.isalpha())
print(f'{n} Only Lowers ?', n.islower())
print(f'{n} Only Alpha Numeric ?', n.isalnum())
print(f'{n} Only Upper ?', n.isupper())
print(f'{n} Is printable ?', n.isprintable())
print(f'{n} Spaces ?', n.isspace())
print(f'{n} Is title ?', n.istitle())
