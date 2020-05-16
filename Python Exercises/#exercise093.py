# exercise093
player = {}
player['name'] = str(input('Name Player: '))
player['matches'] = int(input(f'How many matches {player["name"]} played ? '))
goals = []
for c in range(1, player['matches'] + 1):
    goals.append(int(input(f'How many goals {c}  in the next match ? ')))
    player['goals'] = goals[:]
    player['total'] = sum(goals)
print(player)
print('-=' * 30)
for k, v in player.items():
    print(f'{k} value - {v}')
print('-=' * 30)
print(f'The player {player["name"]} played {player["matches"]} matches.')
for i, v in enumerate(player['goals']):
    print(f'   =>In the match {i+1}, has scored {v} goals.')
print(f'Total of {sum(goals)} goals.')