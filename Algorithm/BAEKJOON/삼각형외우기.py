angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

if angle1 == 60 and angle2 == 60 and angle3 == 60:
    print('Equilateral')

elif angle1 + angle2 + angle3 == 180 and angle1 == angle2:
    print('Isosceles')

elif angle1 + angle2 + angle3 == 180 and angle2 == angle3:
    print('Isosceles')

elif angle1 + angle2 + angle3 == 180 and angle1 == angle3:
    print('Isosceles')

elif angle1 + angle2 + angle3 == 180 and angle1 != angle2 != angle3:
    print('Scalene')

else:
    print('Error')