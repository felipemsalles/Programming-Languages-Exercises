# exercise101
def vote(birth):
    from datetime import date
    current = date.today().year
    age = current - birth
    if age >= 65 or 16 <= age < 18:
        return f'{age} years old. Category: OPTIONAL. '
    elif age >= 18 and age < 65:
        return f'{age} years old. Category:  OBLIGATORY .'
    else:
        return f'{age} years old. Category: YOU DO NOT VOTE YET(UNDERAGE).'


# Main Program
birth = int(input('Year of Birth: '))
print(vote(birth))