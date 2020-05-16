# exercise064
count = sum = num = 0
num = int(input('Enter a number: '))
while num != 999:
    count += 1
    sum += num
    num = int(input('Enter a number: '))
print(f'Number of terms = {count} and the sum of terms = {sum}.')