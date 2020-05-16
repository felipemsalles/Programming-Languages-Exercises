# exercise077
words = ('LEARN', 'PROGRAMMING', 'LANGUAGE', 'PYTHON', 'COURSE', 'FREE',
         'STUDY', 'PRACTICE', 'WORK', 'MARKET', 'PROGRAMMER', 'FUTURE')
for w in words:
    print(f'\nOn the word {w} we have ', end='')
    for word in w:
        if word.lower() in 'aeiou':
            print(word, end=' ')
