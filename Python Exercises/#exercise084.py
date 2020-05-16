# exercise084
temp = []
contracted = []
higher = lower = 0
while True:
    temp.append(str(input('Enter your name: ')))
    temp.append(float(input('Enter your weight: ')))
    if len(contracted) == 0:
        higher = lower = temp[1]
    else:
        if temp[1] > higher:
            higher = temp[1]
        if temp[1] < lower:
            lower = temp[1]
    contracted.append(temp[:])
    temp.clear()
    option = str(input('Do you want to continue ? [Y/N]')).upper().strip()[0]
    if option in 'Nn':
        break
print(f'a)Total of people contracted: {len(contracted)}.')
print(f'b) Higher weight {higher} kg. Weight of ', end='')
for p in contracted:
    if p[1] == higher:
        print(f'{[p[0]]} ', end='')
print()
print(f'c) Lower weight {lower} kg. Weight of ', end='')
for p in contracted:
    if p[1] == lower:
        print(f'{[p[0]]} ', end='')