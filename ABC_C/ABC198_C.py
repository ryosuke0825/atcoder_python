from math import sqrt

R, X, Y = map(int, input().split())

k = sqrt(X**2+Y**2)
if k % R == 0:
    print(int(k//R))
elif k < R:
    print(2)
else:
    print(int(k//R+1))
