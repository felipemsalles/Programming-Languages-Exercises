# exercise056

total = 0
age_average = 0
men_majority = 0
old_name = ''
women_total20 = 0
for n in range(1, 5):
    name = str(input('Enter your name: ')).strip()
    age = int(input('Enter your age: '))
    gender = str(input('Enter your gender [M] - Male [F] - Female: ')).strip()
    total += age
    if n == 1 and gender in 'Mm':
        men_majority = age
        old_name = name
    if gender in 'Mm' and age > men_majority:
        men_majority = age
        old_name = name
    if gender in 'Ff' and age < 20:
        women_total20 += 1
age_average = total / 4
print(f'The age average = {age_average}.')
print(f'The older man has {men_majority} years old and he is {old_name}.')
print(f'Womens under 20 years old = {women_total20}.')
