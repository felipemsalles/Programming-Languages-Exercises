# exercise076

tuple = ('Pencil', 1.75, 'Eraser', 2.00, 'Notebook', 15.90, 'Box', 25.00, 'Ruler', 4.20, 'Scissors',
         9.99, 'Bag', 120.32, 'Pens', 22.30, 'Book', 34.90)
print('-' * 30)
print('                 PRICE LIST                      ')
print('-' * 30)
print(f'{tuple[0]}........................ $ {tuple[1]:.2f}')
print(f'{tuple[2]}........................ $ {tuple[3]:.2f}')
print(f'{tuple[4]}........................ $ {tuple[5]:.2f}')
print(f'{tuple[6]}........................ $ {tuple[7]:.2f}')
print(f'{tuple[8]}........................ $ {tuple[9]:.2f}')
print(f'{tuple[10]}....................... $ {tuple[11]:.2f}')
print(f'{tuple[12]}....................... $ {tuple[13]:.2f}')
print(f'{tuple[14]}....................... $ {tuple[15]:.2f}')
print(f'{tuple[16]}....................... $ {tuple[17]:.2f}')
print('-' * 30)

# Course Solution
list_price = ('Pencil', 1.75,
              'Eraser', 2.00,
              'Notebook', 15.90,
              'Box', 25.00,
              'Ruler', 4.20,
              'Scissors', 9.99,
              'Bag', 120.32,
              'Pens', 22.30,
              'Books', 34.90)
print('-' * 40)
print(f'{"PRICE LIST":^40}')
print('-' * 40)
for pos in range(0, len(list_price)):
    if pos % 2 == 0:
        print(f'{list_price[pos]:.<30}', end='')
    else:
        print(f'R${list_price[pos]:>7.2f}')
print('-' * 50)