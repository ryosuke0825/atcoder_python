n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += bl[al[i]-1]
    if 1 <= i and al[i] == al[i-1]+1:
        ans += cl[al[i-1]-1]

print(ans)
