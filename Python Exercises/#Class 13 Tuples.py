snack = ('Burguer', 'Juice', 'Pizza', 'Fries')
# Tuples are immutable
# snack[1] = 'Soda'
# It is not possible to assign values to the tuple except in its declaration.
print(snack)

# 1
for food in snack:
    print(f'I am going to eat {food}')
print('I had a very good meal!')
print(len(snack))

# 2
for count in range(0, len(snack)):
    print(snack[count])
# 3 - position
for count in range(0, len(snack)):
    print(f'I am going to eat {snack[count]} - position {count}')
# 4 - position
for pos, food in enumerate(snack):
    print(f'I am going to eat {food} - position {pos}.')

print('I had a very good meal!')
print('-' * 20)
print(sorted(snack))
print('-' * 20)


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))
print(c.index(5, 1))  # print the position of the second number 5.
#

person = ('Jack', 20, 'M', 80.00)
print(person)

#
person = ('Jack', 20, 'M', 80.00)
del(person)    # delete
print(person)
