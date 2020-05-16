# exercise044
price = float(input('Enter the price of the product: '))
discount_1x = price - (price * 0.1)
discount_1x_creditcard = price - (price * 0.05)
creditcard_3x_more = price + (price * 0.2)
option = int(input('Enter your payment option: '))
print("""
[0] 1x money = 10% of discount.
[1] 1x credit card = 5% of discount.
[2] 2x credit card = Normal Price.
[3] 3x or more = 20% of Taxes.
""")
if option == 0:
    print(f'The price of the product is {price} and the final price is: {discount_1x}')
elif option == 1:
    print(f'The price of the product is {price} and the final price is: {discount_1x_creditcard}')
elif option == 2:
    print(f'The price of the product is {price} and the final price is: {price}')
elif option == 3:
    print(f'The price of the product is {price} and the final price is: {creditcard_3x_more}')
else:
    print(f'Try again!')