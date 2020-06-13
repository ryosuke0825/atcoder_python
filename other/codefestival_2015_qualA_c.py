import sys


def input():
    return sys.stdin.readline()[:-1]


N, T = map(int, input().split())
A = [0]*N
B = [0]*N
AB = []
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b
    AB.append(a-b)

# 全部写しても間に合わない時
sum_b = sum(B)
if T < sum_b:
    print(-1)
    exit(0)

AB.sort(reverse=True)
sum_a = sum(A)
ans = 0
for i in range(N):
    if sum_a <= T:
        break
    sum_a -= AB[i]
    ans += 1
print(ans)
