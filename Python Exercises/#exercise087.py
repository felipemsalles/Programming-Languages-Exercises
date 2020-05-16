# exercise087
sum_even = higher = sum_column = 0
matrix_maths = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for r in range(0, 3):
    for c in range(0, 3):
        matrix_maths[r][c] = int(input(f'Enter a number for position: [{r}],[{c}]:'))
for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix_maths[r][c]:^5}]', end='')
        if matrix_maths[r][c] % 2 == 0:
            sum_even += matrix_maths[r][c]
    print()
print(f'Sum of even values: {sum_even}')
for r in range(0, 3):
    sum_column += matrix_maths[r][2]
print(f'Sum of third column values: {sum_column}')
for c in range(0, 3):
    if c == 0:
        higher = matrix_maths[1][c]
    elif matrix_maths[1][c] > higher:
        higher = matrix_maths[1][c]
print(f'c) Higher Value of Second Row: {higher}.')