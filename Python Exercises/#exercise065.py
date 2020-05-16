# exercise065
sum = quantity = average = higher = lower = 0
answer = 'Y'
while answer in 'Yy':
    num = int(input('Enter a number: '))
    sum += num
    quantity += 1
    if quantity == 1:
        higher == lower == num
    else:
        if num > higher:
            higher = num
        if num < lower:
            lower = num
    option = str('Do you want to continue? [Y/N]').upper().strip()[0]
average = sum / quantity
print(f'Total of numbers = {quantity}. Average = {average}.')
print(f'Higher = {higher}| Lower = {lower}. ')