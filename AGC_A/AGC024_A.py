a, b, c, k = map(int, input().split())

line = 10*18
for _ in range(k):
    tmpa = b+c
    tmpb = a+c
    tmpc = a+b
    a = tmpa
    b = tmpb
    c = tmpc
    if a-b > line:
        print('Unfair')
        exit(0)
print(a-b)
