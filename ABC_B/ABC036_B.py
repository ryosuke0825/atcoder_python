n = int(input())

sl = []
for _ in range(n):
    sl.append(list(input()))

for i in range(n):
    ans = []
    for j in range(n):
        ans.append(sl[len(sl)-j-1][i])
    print("".join(ans))
