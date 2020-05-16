# Class 20 Functions Part 1 - Python Course.
def counter(*num):
    for value in num:
        print(value, end=' ')
    print('THE END!')


counter(2, 1, 7)
counter(8, 0)
counter(4, 4, 7, 6, 2)


print('-' * 30)


def counter(*num):
    size = len(num)
    print(f'Values typed: {num}. The total of numbers is {size} numbers.')


counter(2, 1, 7)
counter(8, 0)
counter(4, 4, 7, 6, 2)
print('-' * 30)



def double(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1



values = [6, 3, 9, 1, 0, 2]
double(values)
print(values)




# Class 21 Functions Part 2 - Python Course.
help(print)   # interactive help fora do python console
print(input.__doc__)
help(input)


# Doc strings
def counter(s, e, p):
    """
    ->The program print a count of numbers.
    :param s: the start
    :param e: the end
    :param p: pass
    :return: sem retorno
    Função Criada por Felipe.
    """
    c = sum
    while c <= e:
        print(f'{c}', end=' ')
        c += p
    print('FIM')


help(counter)


# Optionals Parameters
def sum(a, b, c=0):
    sum = a + b + c
    print(f'The sum = {sum}.')


sum(3, 2, 5)
sum(8, 4)




# Scope of Variables


def test():
    x = 8
    print(f'On the test function, n = {n}.')
    print(f'On the test function, x = {x}.')  # local scope (inside the function)



# Main Program
n = 2
print(f'On the main program, n = {n}.') # 'n' is a global variable.
test()

# Another test using 2 variables, one local and the other global.
def function():
    n1 = 4
    print(f'N1 inside = {n1}')

n1 = 2
function()
print(f'N1 outside = {n1}')


# Returning Values
def sum(a=0, b=0, c=0):
    s = a + b + c
    return s


test1 = sum(3, 2, 5)
test2 = sum(8, 4)
test3 = sum(6)
print(f'Results: {test1}, {test2} and {test3}.')


# Practice Part

# Factorial
def factorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Enter a number: '))
print(f'The factorial of {n} = {factorial(n)}.')

# Without using parameters
f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()
print(f'Results: {f1}, {f2} and {f3}.')


# Even - Odd Program
def even(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Enter a number: '))
print(even(num))
if even(num):
    print('EVEN!')
else:
    print('NOT EVEN!')



