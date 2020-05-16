# exercise105
def grades(*n, sit=False):
    """
    ->Analyze grades of students.
    n: one or more grades.
    sit: situation of the student.
    return: dictionary.
    """
    a = {}
    a['total'] = len(n)
    a['higher'] = max(n)
    a['lower'] = min(n)
    a['average'] = sum(n)/len(n)
    if sit:
        if a['average'] >= 7:
            a['situation'] = 'GOOD'
        elif a['average'] >= 5:
            a['situation'] = 'MEDIUM'
        else:
            a['situation'] = 'BAD'
    return a


# Main Program
a = grades(5.5, 2.5, 1.5, sit=True)
print(a)