n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    str_i = str(i)
    sum = 0
    for j in range(len(str_i)):
        sum += int(str_i[j])
    if a <= sum <= b:
        ans +=i

print(ans)
