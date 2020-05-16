def increase(price=0, tax=0, f=False):
    answer = price + (price * tax / 100)
    return answer if f is False else coin(answer)


def reduce(price=0, tax=0, f=False):
    ans = price - (price * tax / 100)
    return ans if f == False else coin(ans)

def double(price=0, f=False):
    answer = price * 2
    return answer if not f else coin(answer)


def half(price=0, f=False):
    ans = price / 2
    return ans if f is False else coin(ans)


def coin(price=0, coin='$'):
    return f'{coin}{price:.2f}'.replace('.', ',')