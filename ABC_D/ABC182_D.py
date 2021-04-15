N = int(input())
A = list(map(int, input().split()))

ac = [0]*(N)
ac[0] = A[0]
ac_max = [0]*(N)
ac_max[0] = max(0, A[0])
for i in range(1, N):
    ac[i] = ac[i-1]+A[i]
    ac_max[i] = max(ac_max[i-1], ac[i])


now_place = 0
ans = 0
for i in range(N):
    ans = max(ans, now_place+ac_max[i])
    now_place += ac[i]

print(ans)
