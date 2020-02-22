n = int(input())
x = list(map(int, input().split()))

ans = -1
for i in range(max(x)):
    tmp_ans = 0
    for j in range(n):
        tmp_ans += (x[j]-(i+1))**2
    if ans == -1:
        ans = tmp_ans
    else:
        ans = min(ans, tmp_ans)
print(ans)
