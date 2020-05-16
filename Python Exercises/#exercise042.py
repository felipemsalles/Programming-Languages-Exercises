# exercise042
straight_line1 = float(input('Enter the length of the first straight line: '))
straight_line2 = float(input('Enter the length of the second straight line: '))
straight_line3 = float(input('Enter the length of the third straight line: '))
condition1 = abs(straight_line2 - straight_line3) < straight_line1 < straight_line2 + straight_line3
condition2 = abs(straight_line1 - straight_line3) < straight_line2 < straight_line1 + straight_line3
condition3 = abs(straight_line1 - straight_line2) < straight_line3 < straight_line1 + straight_line2

if straight_line1 < straight_line2 + straight_line3 and straight_line2 < straight_line1 + straight_line3  and straight_line3  < straight_line1 + straight_line2:
    print('Can form Triangle!')
    if condition1 != condition2 != condition3 != condition1:
        print(f'Scalene Triangle.')
    elif condition1 == condition2 == condition3:
        print(f'Equilateral Triangle.')
    else:
        print(f'Isosceles Triangle.')
else:
    print('Try again!')