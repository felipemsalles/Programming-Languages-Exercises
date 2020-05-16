# exercise092
from datetime import date
current = date.today().year
data = {}
data['Name'] = str(input('Digite seu nome: '))
data['Birth'] = int(input('Digite seu ano de nascimento: '))
data['Age'] = current - data['Birth']
data['Work Permit'] = int(input('Work Permit (0 do not have): '))
while data['Work Permit'] != 0:
    data['Hiring'] = int(input('Year of Hiring: '))
    data['Salary'] = float(input('Salary: $ '))
    data['Retirement'] = (35 - (current - data['Hiring'])) + data['Age']
    for k, v in data.items():
        print(f' - {k} value - {v}')
    break