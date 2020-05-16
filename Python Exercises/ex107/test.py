# exercise110
from ex107 import coin

# Main Program
p = float(input('Enter the price: $ '))
print(f'The half of $ {p} is {coin.half(p)}')
print(f'The double of $ {p} is {coin.double(p)}')
print(f'Increasing 10%, we have $ {coin.increase(p, 10)}')