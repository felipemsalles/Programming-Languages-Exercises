# exercise071
value = int(input('Enter the value of your withdrawal:$ '))
total = value
ballot = 50
total_ballot = 0
while True:
    if total >= ballot:
        total -= ballot
        total_ballot += 1
    else:
        if total_ballot > 0:
            print(f'Total {total_ballot} of ballots of ${ballot}.')
        if ballot == 50:
            ballot = 20
        elif ballot == 20:
            ballot = 10
        elif ballot == 10:
            ballot = 1
        total_ballot = 0
        if total == 0:
            break
print('THANKS!')