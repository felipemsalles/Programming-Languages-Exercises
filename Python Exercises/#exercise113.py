# exercise113
def readint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERROR! Enter a valid number.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUser did not enter this number.\033[m')
            return 0
        else:
            return n


def readFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERROR! Enter a valid number.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUser did not enter this number.\033[m')
            return 0
        else:
            return n


# Main Program
num = readint('Enter a value: ')
num2 = readFloat('Enter a real value: ')
print(f'The value was {num} and the real value: {num2}.')