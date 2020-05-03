X = int(input())

for a in range(-500, 500):
    for b in range(-500, 500):
        if (a**5)-(b**5) == X:
            print(a, b)
            exit(0)
