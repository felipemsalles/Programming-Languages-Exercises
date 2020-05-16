from ex115.lib.interface import *


def existentFile(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Error!')
    else:
        print(f'File {name}.txt created!')


def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('Error!')
    else:
        head('PEOPLE REGISTERED')
        for line in a:
            data = linha.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} years')
    finally:
        a.close()


def register(arq, name='unknown', age=0):
    try:
        a = open(arq, 'at')
    except:
        print('Error!')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('Error!')
        else:
            print(f'New register {name} added.')
            a.close()