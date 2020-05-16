from time import sleep
# exercise090

student = {}
student['name'] = str(input('Name: '))
student['average'] = float(input(f'Average of {student["name"]}: '))
if student['average'] >= 7:
    student['situation'] = 'Approved'
elif 5 <= student['average'] < 7:
    student['situation'] = 'Educational Recovery'
else:
    student['situation'] = 'Failed'
print('=' * 30)
sleep(1)
for k, v in student.items():  # for each key one value for student
    print(f' - {k} is equal {v}')
sleep(1.2)
print('Thanks...')