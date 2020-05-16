# exercise067
count = 0
while True:
    num = int(input('Enter a number to print the multiplication table (NEGATIVE TO STOP): '))
    if num < 0:
        break
    for count in range(1, 11, 1):
        print(f'{num} X {count} = {num * count}')
print('THE END')