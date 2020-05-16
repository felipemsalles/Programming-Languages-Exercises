# exercise022
name = str(input('Enter your full name:')).strip()
uppercase = name.upper()
lowercase = name.lower()
length = (len(name)-name.count(' '))
first = name.split()
print(f'The full name is: {name}\n in uppercase: {uppercase}\n in lowercase: {lowercase}\n length: {length}\n first name: {first[0]},'
      f'e a quantidade é: {len(first[0])}')








