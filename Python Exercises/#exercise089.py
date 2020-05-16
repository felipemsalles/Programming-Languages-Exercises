# exercise089
from time import sleep
sheet = []
while True:
    name = str(input('Enter your name: '))
    grade1 = float(input('Enter your first grade:'))
    grade2 = float(input('Enter your second grade: '))
    average = (grade1 + grade2) / 2
    sheet.append([name, [grade1, grade2], average])
    answer = str(input('Do you want to continue [Y/N] ?: ')).upper().strip()[0]
    if answer in 'Nn':
        break
print('LOADING YOUR REPORT CARD ...')
sleep(1)
print(f'{"ID":<4}{"NAME":<10}{"AVERAGE":>8}')
for i, a in enumerate(sheet):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    option = int(input('What student grade do you want to print  ? (999 stop): '))
    if option == 999:
        break
    if option <= len(sheet) - 1:
        print(f'Grades of {sheet[option][0]} are {sheet[option][1]} ')
print('ENDING...')
sleep(1)
print('THANKS!')