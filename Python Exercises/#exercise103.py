# exercise103
def sheet(jog='<unknown>', gol=0):
    print(f'The player {jog} scored {gol} goal(s).')


# Main Program
n = str(input('Player Name: '))
g = str(input('Goals Numbers: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    sheet(goal=g)
else:
    sheet(n, g)
