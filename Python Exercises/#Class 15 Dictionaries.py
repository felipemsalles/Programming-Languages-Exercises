# Class 19 - Python
people = {'name': 'Jack', 'gender':'M', 'age': 20}
print(people['age'])
print(f'{people["name"]} has {people["age"]} years old.')
print(people.keys())
print(people.values())
print(people.items())

print('USING LOOPS...')

for k, v in people.items():
    print(f'{k} = {v}')
print('CHANGING ELEMENT...')
people['name'] = 'Jackson'

for k, v in people.items():
    print(f'{k} = {v}')

print('ADDING ELEMENT...')
people['weight'] = 98.5

for k, v in people.items():
    print(f'{k} = {v}')

print('DEL ELEMENT...')
del people['gender']

for k, v in people.items():
    print(f'{k} = {v}')

print('-' * 20)
brazil = []
state1 = {'uf': 'Rio de Janeiro', 'code': 'RJ'}
state2 = {'uf': 'São Paulo', 'code': 'SP'}
brazil.append(state1)
brazil.append(state2)
print(brazil)
print(brazil[0]['uf'])
print(brazil[1]['code'])
print('-' * 20)
state = dict()
brazil = list()
for c in range(0, 3):
    state['uf'] = str(input('UF: '))
    state['code'] = str(input('State Code: '))
    state.append(state.copy())
for e in state:
    for v in e.values():
        print(f'{v}', end=' ')