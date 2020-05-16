# exercise034
salary = float(input('Enter your salary: '))
ten_percent = salary * 0.1
fifteen_percent = salary * 0.15
if salary > 1250.00:
    print(f'Your salary of {salary} will increase $ {ten_percent}.')
else:
    print(f'Your salary of {salary} will increase $ {fifteen_percent}.')