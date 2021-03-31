import itertools

N, K = map(int, input().split())

routes = [i for i in range(1, N)]
T = []
for i in range(N):
    t = list(map(int, input().split()))
    T.append(t)

# 1都市目～1都市目までの間の全てのルートの組み合わせを作る
all_route = list(itertools.permutations(routes))

# 全ルートを試す
ans = 0
for rotes in all_route:
    time = 0
    s = 0
    for i in range(N-1):
        time += T[s][rotes[i]]
        s = rotes[i]
    time += T[s][0]

    if time == K:
        ans += 1
print(ans)
