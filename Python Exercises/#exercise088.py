# exercise088
from time import sleep
from random import randint
list = []
games = []
count = 0
print('-------GAME-LOTTERY--------')
print('Initiating...')
sleep(1)
n = int(input('How many games do you want to be sorted? '))
tot = 1
while tot <= n:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in list:
            list.append(num)
            count += 1
        if count >= 6:
            break
    list.sort()
    games.append(list[:])
    list.clear()
    tot += 1
print(f'SORTING {n} GAMES...')
for i, l in enumerate(games):
    print(f'Game {i + 1}: {l}')
    sleep(1.2)
sleep(0.2)
print('--------------- GOOD LUCK! ----------------------')