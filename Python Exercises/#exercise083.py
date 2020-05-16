# exercise083
expr = str(input('Enter the expression: '))
stack = []
for symbol in expr:
    if symbol == '(':
        stack.append('(')
    elif symbol == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break
if len(stack) == 0:
    print('Correct expression!')
else:
    print('Incorrect expression.')
