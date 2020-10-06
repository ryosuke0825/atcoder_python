N, M = map(int, input().split())
A = set(list(map(int, input().split())))
B = list(map(int, input().split()))

ans = []
for b in B:
    if b in A:
        ans.append(b)

ans = list(set(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])
