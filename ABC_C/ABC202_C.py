import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

D = [0]*N
for i in range(N):
    D[i] = B[C[i]-1]

cnt = [0]*N
for d in D:
    cnt[d-1] += 1

ans = 0
for a in A:
    ans += cnt[a-1]
print(ans)
