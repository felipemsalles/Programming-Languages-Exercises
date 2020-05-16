# exercise037
num = int(input('Enter a number: '))
print('Menu Options: ')
print("""
[1] - Binary 
[2] - Octal 
[3] - Hexadecimal
""")
option = int(input('Enter your option type: '))
if option == 1:
    print(f'The number {num} in binary is: {bin(num)[2:]}')
elif option == 2:
    print(f'The number {num} in octal is: {oct(num)[2:]}')
elif option == 3:
    print(f'The number {num} in hexadecimal: {hex(num)[2:]}')
else:
    print('Try again!')