# exercise095
team = []
player = {}
goals = []
while True:
    player.clear()
    player['name'] = str(input('Player name: '))
    player['matches'] = int(input(f'How many matches {player["name"]} played ? '))
    goals.clear()
    for c in range(1, player['matches'] + 1):
        goals.append(int(input(f'Quantos gols na partida {c} ? ')))
    player['goals'] = goals[:]
    player['total'] = sum(goals)
    team.append(player.copy())
    while True:
        answer = str(input('Do you want to continue ?[Y/N]: ')).upper()[0]
        if answer in 'YN':
            break
        print('ERROR! Please, enter Y or N.')
    if answer == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(team):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    search = int(input('Which player do you want to see his information ?(999 to stop): '))
    if search == 999:
        break
    if search >= len(team):
        print(f'ERROR! Code do not exist {search}!')
    else:
        print(f' -- PLAYER SEARCH {team[search]["name"]}')
        for i, g in enumerate(team[search]['goals']):
            print(f'    In the game {i} scored {g} goals.')
    print('-' * 40)
print('Thanks...')
