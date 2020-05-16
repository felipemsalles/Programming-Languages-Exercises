def increase(price=0, tax=0, f=False):
    answer = price + (price * tax / 100)
    return answer if f is False else coin(answer)


def reduce(price=0, tax=0, f=False):
    answer = price - (price * tax / 100)
    return answer if f == False else coin(answer)

def double(price=0, f=False):
    answer = price * 2
    return answer if not f else coin(answer)


def half(price=0, f=False):
    answer = price / 2
    return answer if f is False else coin(answer)


def coin(price=0, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.', ',')


def summary(price=0, tax=10, taxr=5):
    print('-' * 30)
    print('SUMMARY OF THE VALUE'.center(30))
    print('-' * 30)
    print(f'Analyzed Price: \t{coin(price)}')
    print(f'Double of Price: \t{double(price, True)}')
    print(f'Half of Price: \t{half(price, True)}')
    print(f'{tax}% of increase: \t{increase(price, tax, True)}')
    print(f'{taxr}% of discount: \t{reduce(price, taxr, True)}')
    print('-' * 30)
    return