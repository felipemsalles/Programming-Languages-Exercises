# exercise031

distance = float(input('Enter the distance in kilometers: '))
print('Short trips-until 200km = $ 0.50 per Km and long trips-over 200km = $ 0.45 per Km ')
short = (distance * 0.50)
long = (distance * 0.45)
if distance <= 200:
    print(f'The price of your trip is: {short}')
else:
    print(f'The price of your trip is: {long}')