# exercise053
phrase = str(input('Enter a phrase: ')).upper().strip()
words = phrase.split()
together = ''.join(words)
inverse = ''
for word in range(len(together)-1, -1, -1):
    inverse += together[word]
if inverse == together:
    print('IT IS A PALINDROME!')
else:
    print('IT IS NOT A PALINDROME!')




