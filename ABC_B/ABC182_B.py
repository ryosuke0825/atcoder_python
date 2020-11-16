N = int(input())
A = list(map(int, input().split()))

ans = 0
ans_max = 0

for k in range(2, 1001):
    cnt = 0
    for a in A:
        if a % k == 0:
            cnt += 1
    if cnt > ans_max:
        ans = k
        ans_max = cnt
print(ans)
