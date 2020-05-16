# exercise024

city = str(input('Enter the name of your city: ')).strip().upper().split()
search = ('NEW' in city[0])
print(f'The name of the city is: {city} and the result of the search of the word is: {search}')