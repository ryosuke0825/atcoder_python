N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    while True:
        if H[i] <= 0:
            break

        base = H[i]
        for j in range(i+1, N):
            # 花の高さが0なら初期のまま
            if H[j] <= 0:
                break

            # 次の花(j+1)が基準の花(j)以下か
            if base <= H[j]:
                H[j] -= 1
            else:
                break
        H[i] -= 1
        ans += 1

ans += max(0, H[-1])
print(ans)
