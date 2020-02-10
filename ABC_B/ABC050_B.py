n = int(input())
tl = list(map(int, input().split()))
m = int(input())
sum_time = sum(tl)
for _ in range(m):
    p, x = map(int, input().split())
    print(sum_time - tl[p-1] + x)
