# exercise050
sum = 0
count = 0
for n in range(0, 6, 1):
    num = int(input(f'Enter a number: '))
    if num % 2 == 0:
        sum += num
        count += 1
print(f'Even numbers {count} result = {sum}.')