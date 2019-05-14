N, M = map(int, input().split())
AB = []
for _ in range(N):
    li = list(map(int, input().split()))
    AB.append(li)

AB.sort()

ans = 0
count = 0
for li in AB:
    if M - count >= li[1]:
        count += li[1]
        ans += li[0]*li[1]
    else:
        ans += li[0]*(M-count)
        break

print(ans)
