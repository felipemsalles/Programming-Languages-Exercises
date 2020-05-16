# exercise075
create_tuple = (int(input('Enter a number: ')),
                int(input('Enter another number: ')),
                int(input('Enter another number: ')),
                int(input('Enter the last number: ')))

print(f'TUPLE: {create_tuple}')
print(f'a) Number 9 in Tuple: {create_tuple.count(9)} times.')
if 3 in create_tuple:
    print(f'b) The position of the first 3 was: {create_tuple.index(3) + 1}')
else:
    print(f'b) The value 3 is not entered.')
print(f'c) Even Numbers: ', end='')
for num in create_tuple:
    if num % 2 == 0:
        print(num, end=' ')