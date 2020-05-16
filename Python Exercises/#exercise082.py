# exercise082
values = []
evens = []
odds = []
while True:
    n = int(input('Digite um valor:'))
    values.append(n)
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)
    answer = str(input('Do you want to continue [Y/N]?: ')).upper().strip()[0]
    if answer in 'Nn':
        break
print(f'List...                     ->     {values}')
print(f'List of Even Numbers...     ->     {evens}')
print(f'List of Odd Numbers...      ->     {odds}')
print('-' * 30)

# Course Solution
num = list()
even = list()
odd = list()
while True:
    num.append(int(input('Enter a value: ')))
    answer = str(input('Do you want to continue [Y/N]?: ')).upper().strip()[0]
    if answer in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
       even.append(v)
    elif v % 2 == 1:
        odd.append(v)
print(f'List   {num}.')
print(f'Even List   {even}.')
print(f'Odd List {odd}.')