# exercise094
people = {}
data = []
sum = average = 0
while True:
    people.clear()
    people['name'] = str(input('Enter your name: '))
    while True:
        people['gender'] = str(input('Enter your gender [M/F]: ')).upper().strip()[0]
        if people['gender'] in 'MF':
            break
        print('ERROR! Please, enter only M or F.')
    people['age'] = int(input('Enter your age: '))
    sum += people['age']
    data.append(people.copy())
    while True:
        resp = str(input('Do you want to continue ? [Y/N]')).strip().upper()[0]
        if resp in 'YN':
            break
        print('ERROR! Please, enter only Y or N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'a){len(data)} people registered.')
average = sum / len(data)
print(f'b) Age average: {average:5.2f} years')
print('c) Women registered', end='')
for p in data:
    if p['gender'] == 'F':
        print(f'{p["name"]}', end='')
print()
print('d) People over the average: ')
for p in data:
    if p['age'] >= average:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<END>>>')