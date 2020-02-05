a, b, k = map(int, input().split())

ans = []
for i in range(a, a+k):
    if i > b:
        break
    ans.append(i)

for i in range(b-k+1, b+1):
    if i < a:
        break
    if not(i in ans):
        ans.append(i)

for i in ans:
    print(i)
