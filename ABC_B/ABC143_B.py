n = int(input())
d_list = list(map(int, input().split()))

ans = 0
for i in range(0, len(d_list)-1):
    for j in range(i+1, len(d_list)):
        ans += d_list[i]*d_list[j]

print(ans)
