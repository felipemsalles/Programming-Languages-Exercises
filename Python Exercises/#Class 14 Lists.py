# Python Course - Lists Part 1
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)  # add the value 7
num.sort(reverse=True)
num.insert(2, 2)

if 5 in num:
    num.remove(5)
else:
    print('I did not find the number 5.')
# num.pop(2)
print(num)
print(f'Number of elements = {len(num)}.')
print('-' * 30)
values = list()
for cont in range(0, 5):
    values.append(int(input('Enter a number: ')))
# values.append(5)
# values.append(9)
# values.append(4)
for c, v in enumerate(values):
    print(f'Position {c} - value = {v}!')
print('The end of the list.')
print('-' * 30)


a = [2, 3, 4, 7]
b = a[:]   # copy list a in b
b[2] = 8
print(f'List A: {a}')
print(f'List B: {b}')


# Class 18 - Lists Part 2
test = list()
test.append('Jackson')
test.append(20)
guys = list()  # another list
guys.append(test[:])
test[0] = 'Morgan'
test[1] = 22
guys.append(test[:])
print(guys)
print('-' * 30)
guys = [['Jack', 19], ['Emma', 33], ['Erik', 13], ['Broke', 45]]  # 4 structures inside another one.
print(guys[0])  # print all data of the first structure.
print(guys[0][0])  # print the first item of the structure: Jack.
for p in guys:
    print(f'{p[0]} has {p[1]} years old.')
print('-' * 30)
guys = list()
dice = list()
legal_age = underage = 0
for c in range(0, 3):
    dice.append(str(input('Name: ')))
    dice.append(int(input('Age: ')))
    guys.append(dice[:])
    dice.clear()
print(guys)
for p in guys:
    if p[1] >= 21:
        print(f'{p[0]} is of legal age of majority.')
        legal_age += 1
    else:
        print(f'{p[0]} is underage.')
        legal_age += 1
print(f'Total of legal age {legal_age} and total of underage {underage}.')