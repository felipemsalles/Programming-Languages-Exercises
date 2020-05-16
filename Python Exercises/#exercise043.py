# exercise043
weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))
bmi = weight / (height * height)
print(f'Your IMC = {bmi}')
if bmi < 18.5:
    print(f'Category: UNDERWEIGHT.')
elif bmi >= 18.5 and bmi < 25:
    print(f'Category: IDEAL WEIGHT.')
elif bmi >= 25 and bmi < 30:
    print(f'Category: OVERWEIGHT.')
elif bmi >= 30 and bmi < 40:
    print(f'Category: OBESITY.')
elif bmi >= 40:
    print(f'Category: MORBID OBESITY.')
else:
    print(f'Try again.')