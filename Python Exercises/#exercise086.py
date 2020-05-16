# exercise086
matrix_maths = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # first row, second row, third row.
for r in range(0, 3):
    for c in range(0, 3):
        matrix_maths[r][c] = int(input(f'Enter a value for [{r}, {c}]: '))
for r in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix_maths[r][c]:^5}]', end='')
    print()