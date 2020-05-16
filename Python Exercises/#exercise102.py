# exercise102
def factorial(num=1, show=False):
    """
    -> Factorial Number.
    :param num: Num.
    :param show: Print or Not.
    :return: Return Factorial.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Main Program
print(factorial(5, show=True))
help(factorial)
