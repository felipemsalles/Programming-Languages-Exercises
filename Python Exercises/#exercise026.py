# exercise026

phrase = str(input('Enter a phrase:')).upper().strip()
times = phrase.count('A')
initial = phrase.find('A') + 1
last = phrase.rfind('A') + 1
print(f'The phrase is: {phrase}\n The number of times the letter A appears in the phrase is: {times}\n '
      f'The initial position of A is: {initial}\n '
      f'and the last is: {last}')