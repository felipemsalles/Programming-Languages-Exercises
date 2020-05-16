import math
# exercise018
angle = float(input('Enter an angle: '))
sine = math.sin(math.radians(angle))
print(f'The angle of {angle} has sine valuing: {sine:.2f}')
cosine = math.cos(math.radians(angle))
print(f'The angle of {angle} has cosine valuing: {cosine:.2f}')
tangent = math.tan(math.radians(angle))
print(f'The angle of {angle} has tangent valuing: {tangent:.2f}')