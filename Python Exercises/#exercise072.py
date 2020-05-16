# exercise072
counting = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Den', 'Eleven', 'Twelve',
           'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
while True:
    num = int(input('Enter a number between 0 and 20: '))
    if 0 <= num <= 20:
        break
    print('Try again...', end='')
print(f'Number:{(counting[num])}')

