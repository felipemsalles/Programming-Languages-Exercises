# exercise070
total = products = count = lower = 0
cheap = ''
while True:
    name = str(input('Enter the product name: '))
    price = float(input('Enter the price of the product: '))
    count += 1
    total += price
    if price > 1000.00:
        products += 1
    if count == 1 or price < lower:
        lower = price
        cheap = price
    option = ' '
    while option not in 'YN':
        option = str(input('Do you want to continue [Y/N]: ')).strip().upper()[0]
    if option == 'N':
        break
print(f'Total = $ {total}')
print(f'Total over $ 1000,00 = {products}')
print(f'The product {cheap} was the most cheaper and costs {lower}.')