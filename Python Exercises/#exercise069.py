# exercise069
age_majority = men = women = 0
while True:
    age = int(input('DEnter your age: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Enter your gender [M/F]: ')).strip().upper()[0]
    if age >= 18:
        age_majority += 1
    if gender == 'M':
        men += 1
    if gender == 'F' and age < 20:
        women += 1
    answer = ' '
    while answer not in 'YN':
        answer = str(input('Do you want to continue? [Y/N]')).strip().upper()[0]
    if answer == 'N':
        break
print(f'Total of people of age of majority = {age_majority}.')
print(f'Numbers of Men = {men}.')
print(f'Numbers of Women under 20 years = {women}.')