def readMoney(msg):
    valuate = False
    while not valuate:
        n = str(input(msg)).replace(',','.').strip()
        if n.isalpha() or n == '':
            print('\033[0;31mERROR! Enter a valid number.\033[m')
        else:
            valuate = True
            return float(n)