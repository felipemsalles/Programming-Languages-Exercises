# exercise104
def writeint(msg):
    okay = False
    value = 0
    while True:
        n = str(input('Enter a number: '))
        if n.isnumeric():
            value = int(n)
            okay = True
        else:
            print('\033[0;31mERROR! Enter a correct number.\033[m')
        if okay:
            break
    return value


# Main Program
n = writeint('Enter a number: ')
print(f'You entered the number {n}.')