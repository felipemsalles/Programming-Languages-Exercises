from ex108 import coin

# Main Program
p = float(input('Enter the price of the product: $ '))
print(f'The half ${coin.coin(p)} is ${coin.coin(coin.half(p))}.')
print(f'The double {coin.coin(p)} is ${coin.coin(coin.double(p))}.')
print(f'Increasing 10%, ${coin.coin(coin.increase(p, 10))}.')
