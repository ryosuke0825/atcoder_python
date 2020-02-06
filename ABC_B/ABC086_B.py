a, b = input().split()
ab = int(a+b)

if (ab ** .5).is_integer():
    print("Yes")
else:
    print("No")
