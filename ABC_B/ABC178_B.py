A, B, C, D = map(int, input().split())

ans = max(A*C, A*D, B*C, B*D)
if A <= 0 <= B or C <= 0 <= D:
    ans = max(0, ans)
print(ans)
