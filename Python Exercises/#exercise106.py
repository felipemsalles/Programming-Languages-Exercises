# exercise106
def help(com):
    help(command)


def title(msg):
    lenght = len(msg) + 4
    print('~' * lenght)
    print(f'  {msg}')
    print('~' * lenght)


# Main Program
command = ''
while True:
    title('PyHELP')
    command = str(input("Function or Library > "))
    if help.upper() == 'STOP':
        break
    else:
        help(command)
title('SEE YOU SOON')