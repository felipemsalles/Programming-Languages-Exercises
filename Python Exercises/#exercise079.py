# exercise079
new_list = list()
while True:
    n = int(input('Enter a number: '))
    if n not in new_list:
        new_list.append(n)
        print('Successfully added...')
    else:
        print('Doubled value...error!')
    option = str(input('Do you want to continue [Y/N]?')).upper().strip()[0]
    if option in 'Nn':
        break
new_list.sort()
print(new_list)

