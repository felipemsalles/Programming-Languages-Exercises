def increase(price, tax):
    ans = price + (price * tax / 100)
    return ans


def reduce(price, tax):
    ans = price - (price * tax / 100)
    return ans

def double(price):
    ans = price * 2
    return ans


def half(price):
    ans = price / 2
    return ans
