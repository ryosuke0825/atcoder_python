N, K = map(int, input().split())

day = 0
sum_walk = 0
for _ in range(N):
    a = int(input())
    sum_walk += a
    day += 1
    if sum_walk >= K:
        print(day)
        exit(0)

