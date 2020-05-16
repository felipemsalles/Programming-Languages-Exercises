# exercise078
values = []
higher = 0
lower = 0
for c in range(0, 5):
    values.append(int(input(f'Enter a number for position {c}: ')))
    if c == 0:
        higher = lower = values[c]
    else:
        if values[c] > higher:
            higher = values[c]
        if values[c] < lower:
            lower = values[c]
print(f'Full List -> {values}')
print(f'Higher = {higher} - positions ', end='')
for i, v in enumerate(values):
    if v == higher:
        print(f'{i}...', end='')
print()
print(f'Lower = {lower} - positions ', end='')
for i, v in enumerate(values):
    if v == lower:
        print(f'{i}...', end='')
print()