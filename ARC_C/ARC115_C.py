N = int(input())

ans = [0]*N
ans[0] = 1
mn = 1
minpos = 1
for i in range(2, N+1):
    if i % minpos == 0:
        mn += 1
        minpos = i
    ans[i-1] = mn
print(' '.join(map(str, ans)))
