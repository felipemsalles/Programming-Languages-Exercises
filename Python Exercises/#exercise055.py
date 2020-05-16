# exercise055
greater = 0
lower = 0
for g in range(1, 6):
    weight = float(input(f'Weight of {g}: '))
    if g == 1:
        greater = weight
        lower = weight
    else:
        if weight > greater:
            greater = weight
        if weight < lower:
            lower = weight
print(f'The greater weight was {greater} KG.')
print(f'The lower weight was {lower} KG.')