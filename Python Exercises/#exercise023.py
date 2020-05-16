# exercise023

num = int(input('Enter a number between 0 and 9999: '))
u = num // 1 % 10
d = num // 10 % 10
h = num // 100 % 10
t = num // 1000 % 10
print(f'Unit: {u}\n Dozen: {d}\n Hundred: {h}\n Thousand: {t}')
# unit = n[3:]
# dozen = n[2:3]
# hundred = n[1:2]
# thousand = n[0:1]