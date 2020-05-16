# Class 22 Modules and Packages
from useful import numbers
num = int(input('Enter a number: '))
fact = numbers.factorial(num)
print(f'The factorial of {num} is {fact}.')
print(f'The double of {num} is {numbers.double(num)}.')



# from useful import factorial, double - is recommended to avoid.