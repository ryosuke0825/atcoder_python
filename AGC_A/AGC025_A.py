n = list(map(int, list(input())))

if n[0] == 1 and sum(n) == 1:
    print(10)
else:
    print(sum(n))
