XY = input()
x, y = XY.split(".")

if int(y) <= 2:
    print(x + "-")
elif int(y) <= 6:
    print(x)
else:
    print(x + "+")
