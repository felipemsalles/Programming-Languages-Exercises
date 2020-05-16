from ex115.lib.interface import *
from ex115.lib.file import *
from time import sleep

arq = 'python.txt'
if not existentFile(arq):
    createFile(arq)

while True:
    answer = menu(['People registered', 'Register new person', 'Exit'])
    if answer == 1:
        readFile(arq)
    elif answer == 2:
        head('NEW REGISTRATION')
        name = str(input('Name: '))
        age = readInt('Age: ')
        register(arq, name, age)
    elif answer == 3:
        head('Exit!')
        break
    else:
        head('ERROR!')
    sleep(2)