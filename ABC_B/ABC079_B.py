n = int(input())
n0 = 2
n1 = 1

if n == 1:
    print(1)
else:
    for _ in range(1, n):
        n0, n1 = n1, n0+n1
    print(n1)
