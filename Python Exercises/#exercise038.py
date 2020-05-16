# exercise038
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
if num1 > num2:
    print(f'The first number {num1} is higher than the second number {num2}.')
elif num2 > num1:
    print(f'The second number {num2} is higher than the first number {num1}.')
elif num1 == num2:
    print(f'EQUAL NUMBERS: {num1} = {num2} ')
else:
    print(f'Try again!')