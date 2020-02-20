n = int(input())
num = [0, 0, 1]
if n <= 3:
    print(num[n-1])
else:
    a, b, c = 0, 0, 1
    for _ in range(3, n):
        d = (a+b+c) % 10007
        a = b
        b = c
        c = d
    print(d % 10007)
