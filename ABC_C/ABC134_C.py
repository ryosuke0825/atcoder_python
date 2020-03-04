n = int(input())

A = []
max1 = 0
max2 = 0
max1w = False
for _ in range(n):
    a = int(input())
    A.append(a)
    if a > max1:
        max2 = max1
        max1 = a
        max1w = False
    elif a == max1:
        max1w = True
    elif a > max2:
        max2 = a

for a in A:
    if a == max1 and max1w:
        print(max1)
    elif a == max1:
        print(max2)
    else:
        print(max1)
