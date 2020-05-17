import math


A, B, H, M = map(int, input().split())


m = 6*M
if m == 0:
    m = 360

h = 30*H
h += 6*(M/12)
if h == 0:
    h = 360

kakudo = abs(h-m)
print(math.sqrt(A**2+B**2-2*A*B*math.cos(math.radians(kakudo))))
