from heapq import heappush, heappop

N = int(input())
A_to_B = [[] for _ in range(N + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    A_to_B[a].append(b)

q = []
point = 0
for day in range(1, N + 1):
    for b in A_to_B[day]:
        heappush(q, -b)
    point += -heappop(q)
    print(point)
