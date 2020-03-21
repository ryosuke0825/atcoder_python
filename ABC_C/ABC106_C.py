S = list(input())
K = int(input())

if S[:K].count('1') == K:
    print(1)
    exit(0)
for s in S:
    if s != '1':
        print(s)
        exit(0)
