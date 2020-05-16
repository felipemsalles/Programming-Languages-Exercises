# exercise033

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
num3 = int(input('Digite o terceiro número:'))
if num1 == num2 == num3:
    print(f'The 3 numbers are equal!')
if num1 > num2 > num3:
    print(f'The first number {num1} is the highest and the last number is the lowest {num3}.')
if num2 > num1 > num3:
    print(f'The second number {num2} is the highest and the last number is the lowest {num3}.')
if num3 > num1 > num2:
    print(f'The last number {num3} is the highest and the second number is the lowest {num2}.')
if num1 > num3 > num2:
    print(f'The first number {num1} is the highest and the second number is the lowest {num2}.')
if num2 > num3 > num1:
    print(f'The second number {num2} is the highest and the first number is the lowest {num1}.')
if num3 > num2 > num1:
    print(f'The last number {num3} is the highest and the first number is the lowest {num1}.')