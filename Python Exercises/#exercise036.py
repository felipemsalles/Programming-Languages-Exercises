# exercise036
house_price = float(input('Enter the house price:$ '))
salary = float(input('Enter your salary:$ '))
years = int(input('Enter how many years do you want to pay: '))
monthly_payment = house_price / (years * 12)
print(f'To pay a house costing ${house_price:.2f} in {years} years', end='')
print(f'The monthly payment is going to be ${monthly_payment:.2f}')
if monthly_payment > salary * 0.3:
    print('Loan denied.')
else:
    print(f'The monthly payment is going to be$ {monthly_payment:.2f}')








