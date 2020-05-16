# exercise035
straight_line1 = float(input('Enter the length of the first straight line: '))
straight_line2 = float(input('Enter the length of the second straight line: '))
straight_line3 = float(input('Enter the length of the third straight line: '))
condition1 = abs(straight_line2 - straight_line3) < straight_line1 < straight_line2 + straight_line3
condition2 = abs(straight_line1 - straight_line3) < straight_line2 < straight_line1 + straight_line3
condition3 = abs(straight_line1 - straight_line2) < straight_line3 < straight_line1 + straight_line2

if condition1 and condition2 and condition3 == True:
    print('The values tested on the conditions cases can form a triangle!')
else:
    print('The values tested on the conditions cases can not form a triangle!')