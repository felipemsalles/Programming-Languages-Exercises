def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERROR! Enter a valid number.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUser did not enter the number.\033[m')
            return 0
        else:
            return n


def line(length=42):
    return '-' * length


def head(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(list):
    head('MAIN MENU')
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1
    print(line())
    opc = readInt('Your option: ')
    return opc

