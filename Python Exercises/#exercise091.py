# exercise091
from time import sleep
from random import randint
from operator import itemgetter
game = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)
        }
ranking = []
for k, v in game.items():
    print(f'{k} value = {v} dice.')
    sleep(1)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('-----------RANKING OF PLAYERS----------')
for i, v in enumerate(ranking):
    print(f'{i + 1} position: {v[0]} with  {v[1]}.')
