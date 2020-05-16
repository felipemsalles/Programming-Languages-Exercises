# You need to avoid:
print('Hello')
print('Hello')
print('Hello')
print('-' * 10)

# For Loops:
for c in range(0, 6):
    print('Hello!')
print('THE END!')

print('-' * 10)

for c in range(6, 0, -1):
    print(c)
print('THE END!')

print('-' * 10)

for c in range(0, 7, 2):
    print(c)
print('THE END!')

print('-' * 10)

num = int(input('Enter a number: '))
for c in range(0, num + 1):
    print(c)
print('THE END')
print('-' * 10)
start = int(input('Start: '))
end = int(input('End: '))
sequence = int(input('Sequence: '))
for c in range(start, end + 1, sequence):
    print(c)
print('THE END!')

print('-' * 10)

s = 0
for c in range(0, 3):
    n = int(input('Enter a number: '))
    s += n  # sum = sum + n
print(f'The sum of the values = {s}.')