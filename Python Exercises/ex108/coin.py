def increase(price=0, tax=0):
    answer = price + (price * tax / 100)
    return answer


def reduce(price=0, tax=0):
    answer = price - (price * tax / 100)
    return answer


def dobro(price=0):
    answer = price * 2
    return answer


def half(price=0):
    answer = price / 2
    return answer


def coin(price=0, coin='$'):
    return f'{coin}{price:.2f}'.replace('.', ',')