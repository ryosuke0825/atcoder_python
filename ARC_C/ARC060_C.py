N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = T
end_time = t[0]+T
for i in range(1, N):
    if end_time >= t[i]:
        ans += ((t[i]+T)-end_time)
    else:
        ans += T
    end_time = t[i]+T

print(ans)
