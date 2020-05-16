# exercise066
count = sum = 0
while True:
    num = int(input('Enter a number (999 to stop): '))
    if num == 999:
        break
    count += 1
    sum += num
print(f'Total of numbers = {count} | Sum = {sum}.')
