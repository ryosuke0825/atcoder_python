N, M = map(int, input().split())

case = [i for i in range(1, N+1)]
disk = []
for _ in range(M):
    disk.append(int(input()))

now = 0
for d in disk:
    if d == now:
        continue
    i = case.index(d)
    tmp = case[i]
    case[i] = now
    now = tmp

for c in case:
    print(c)
