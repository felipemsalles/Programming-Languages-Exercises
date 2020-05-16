# exercise081
list = []
valor = 5
while True:
   list.append(int(input('Enter a number: ')))
   answer = str(input('Do you want to continue [Y/N]?: ')).upper().strip()[0]
   if answer in 'Nn':
       break
list.sort(reverse=True)
print(f'a) Total of numbers = {len(list)}.')
print(f'b) Descending Order: {list}')
if valor in list:
    print(f'c) 5 is in the list!')
else:
    print(f'c) Could not find 5 in the list!')