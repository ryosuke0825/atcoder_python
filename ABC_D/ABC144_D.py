import math

a, b, x = map(int, input().split())

tan_theta = 2*(b/a-x/math.pow(a, 3))
tan_theta2 = a * pow(b, 2) / (2 * x)

if math.pow(a, 3) / 2 * tan_theta < x:
    theta = math.atan(tan_theta)
else:
    theta = math.atan(tan_theta2)

print(math.degrees(theta))
