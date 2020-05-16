# exercise027

fullname = str(input('Enter your full name: ')).strip()
list = fullname.split()
first = list[0]
last = list[len(fullname)-1]
print(f'The fullname is: {fullname} \n the first is: {first}\n the last is: {last}.')