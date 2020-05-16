# exercise040
grade1 = int(input('Enter your first grade: '))
grade2 = int(input('Enter your second grade:'))
average = (grade1 + grade2) / 2
if average < 5.0:
    print(f'You have failed. Average = {average:.1f}')
elif average >= 5.0 and average <= 6.9:
    print(f'You need to do a educational recovery.Average = {average:.1f}')
elif average >= 7.0:
    print(f'You were approved. Average = {average:.1f}')
else:
    print(f'Try again!')