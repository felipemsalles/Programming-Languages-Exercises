# exercise085
n = []
even = []
odd = []
for v in range(1, 8):
    x = int(input(f'Enter {v} value: '))
    n.append(x)
    if x % 2 == 0:
        even.append(x)
    if x % 2 == 1:
        odd.append(x)
    n.append(even[:])
    n.append(odd[:])
print(f'Values Entered -> {n.append(x)}')
print(f'Even Values    -> {sorted(even)}')
print(f'Odd Values     -> {sorted(odd)}')
print('-' * 30)

# Course Solution
num = [[], []]
value = 0
for c in range(1, 8):
    valor = int(input(f'Enter {c} value: '))
    if valor % 2 == 0:
        num[0].append(value)
    else:
        num[1].append(value)
print(f'All Values: {num}')
print(f'Even Values: {sorted(num[0])}')
print(f'Odd Values: {sorted(num[1])}')