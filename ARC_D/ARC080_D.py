import itertools

H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

one_line = []
for i in range(N):
    s = str(i+1)
    one_line.append([s]*A[i])
li = list(itertools.chain.from_iterable(one_line))

for i in range(0, H):
    tmp = li[i*W:i*W+W]
    if i % 2 != 0:
        tmp = tmp[::-1]
    print(' '.join(list(tmp)))
