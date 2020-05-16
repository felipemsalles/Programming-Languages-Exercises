# exercise057
gender = str(input('Enter your gender [M/F]: ')).upper()[0]
while gender != 'F' and gender != 'M':
    gender = str(input('Try again [M/F]: ')).upper()[0]
print(f'Gender {gender} registered!')
print('The end.')



