# exercise073
rating_table = ('Real Madrid', 'Barcelona', 'PSG', 'Milan', 'Lyon', 'LA Galaxy',
                'Portland Timbers', 'Bayer', 'Liverpool', 'Manchester City', 'Manchester United', 'Chelsea',
                'Porto', 'Ajax', 'Sporting', 'Arsenal', 'Atlanta United', 'Seattle Sounders', 'Toronto FC',
                'New York City FC')
print(f'a) The first teams in the top five : {rating_table[0:5]}')
print(f'b) The last four teams: {rating_table[16:]}')  # or [-4:]
print(f'c) Alphabetical order: {sorted(rating_table)}')
print(f'd) Barcelona is in the {rating_table.index("Barcelona") + 1}ª position.')