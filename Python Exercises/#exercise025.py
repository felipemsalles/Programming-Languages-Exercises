# exercise025

name = str(input('Enter your full name: ')).upper().strip().split()
search = ('JULIA' in name[0:])
print(f'The name of the person is: {name} and the result of the search is: {search}')