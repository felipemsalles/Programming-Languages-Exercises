# exercise039
from datetime import date
current = date.today().year
print(current)
year = int(input('Enter your year of birth: '))
if current - year < 18:
    print(f'You did not complete the age to do your conscription. You have {18 - (current - year)} year(s) to your military conscription.')
elif current - year == 18:
    print(f'It is time to do your military conscription!')
elif current - year > 18:
    print(f'Your conscription is late {(current - year) - 18} year(s). You need to solve this problem!')
else:
    print('Try again!')