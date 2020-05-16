# exercise019
import random
student1 = str(input('Enter the name of the first student: '))
student2 = str(input('Enter the name of the second student: '))
student3 = str(input('Enter the name of the third student: '))
student4 = str(input('Enter the name of the last student: '))
students_list = [student1, student2, student3, student4]
selected = random.choice(students_list)
print(f'The student selected was: {selected}')