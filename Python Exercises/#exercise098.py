# exercise098
from time import sleep
def counter(s, e, p):
        print('-=' * 30)
        print(f'Counting {s} until {e} - {p} - {p}')
        if p < 0:
            p *= -1
        if p == 0:
            p = 1
        if s < e:
            while s <= e:
                print(f'{s}', end=' ')
                sleep(0.5)
                s += p
            print('THE END!')
            sleep(0.2)
            print('-=' * 30)
        else:
            while s >= e:
                print(f'{s}', end=' ')
                sleep(0.5)
                s -= p
            print('THE END!')

# Main Program

print('COUNTER...')
counter(s=1, e=10, p=1)
counter(s=10, e=0, p=2)
print('Now, it is your time!')
counter(s=(int(input('Start: '))), e=(int(input('End: '))), p=(int(input('Pass: '))))