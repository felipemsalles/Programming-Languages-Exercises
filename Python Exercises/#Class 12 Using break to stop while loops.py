num = sum = 0
while True:
    num = int(input('Enter a number: '))
    if num == 999:
        break
    sum += num
print(f'The sum value is {sum}.')
