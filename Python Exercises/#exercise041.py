# exercise041
from datetime import date
current = date.today().year
year = int(input('Digite seu ano de nascimento:'))
age = current - year
print(f'The age of athlete is: {age}.')
if age <= 9:
    print(f'Athlete Category: CHILD.')
elif age <= 14:
    print(f'Athlete Category: KIDS.')
elif age <= 19:
    print(f'Athlete Category: JUNIOR')
elif age <= 20:
    print(f'Athlete Category: SENIOR.')
elif age > 20:
    print(f'Athlete Category: MASTER.')
else:
    print('Try again!')




