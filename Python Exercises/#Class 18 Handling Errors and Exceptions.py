# Class 23 Python Course - Handling Errors and Exceptions
try:
    a = int(input('Numerator: '))
    b = int(input('Denominator: '))
    r = a / b
except:
    print('Program Error :( ')
else:
    print(f'The result is{r:.1f}')
finally:
    print('Thanks!')




# Another Way


try:
    a = int(input('Numerator: '))
    b = int(input('Denominator: '))
    r = a / b
except Exception as error:
    print(f'The problem founded was {error.__class__}')
else:
    print(f'The result is {r:.1f}')
finally:
    print('Thank you!')




#Another Way


try:
    a = int(input('Numerator: '))
    b = int(input('Denominator: '))
    r = a / b
except (ValueError, TypeError):
    print('Value or Type Error.')
except ZeroDivisionError:
    print('Division by zero is impossible.')
except KeyboardInterrupt:
    print('Keyboard interrupt')
except Exception as erro:
    print(f'The error was {erro.__cause__}')
else:
    print(f'The result is {r:.1f}')
finally:
    print('Thank you!')