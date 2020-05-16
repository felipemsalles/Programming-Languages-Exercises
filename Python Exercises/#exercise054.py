# exercise054
from datetime import date
current = date.today().year
total = 0
for c in range(0, 7):
    year_birth = int(input('Enter your year of birth: '))
    if current - year_birth >= 21:
        total += 1
print(f'{total} has reached legal majority and {7- total} not yet.')
