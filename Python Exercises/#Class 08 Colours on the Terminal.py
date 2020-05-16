# print('\033[4;30;45m Hello World!\033[m')
# print('\033[0;33;44mHello World!\033[m')
# a = 3
# b = 5
# print(f'The values are \033[32m{a} and \033[31m{b}!!!')
name = 'Jack'
colours = {'clean':'\033[m',
         'blue':'\033[34m',
         'yellow':'\033[33m',
         'blackandwhite':'\033[7;30m'}
print(f'Hello! It is a pleasure to meet you, {colours["blue"]}{name}{colours["clean"]} !!!')
