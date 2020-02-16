n = int(input())
al = list(map(int, input().split()))

ans = "APPROVED"
for a in al:
    if a % 2 == 0:
        if a % 3 != 0 and a % 5 != 0:
            ans = "DENIED"
            break

print(ans)
