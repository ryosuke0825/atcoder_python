n, k, q = map(int, input().split())
p = [0]*n

for _ in range(q):
    a = int(input())
    p[a-1] += 1

for pp in p:
    if k-q+pp > 0:
        print('Yes')
    else:
        print('No')
