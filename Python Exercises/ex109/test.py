from ex109 import coin

# Main Program
p = float(input('Enter the price: $ '))
print(f'The half of ${coin.coin(p)} is ${(coin.half(p, True))}.')
print(f'The double of {coin.coin(p)} is ${(coin.double(p, True))}.')
print(f'Increasing 10%, ${(coin.increase(p, 10, True))}.')
print(f'Reducing 13%, ${(coin.reduce(p, 13, True))}.')
