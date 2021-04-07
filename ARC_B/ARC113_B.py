A, B, C = map(int, input().split())

A %= 10
if B > 4:
    B = B % 4+4
if C > 4:
    C = C % 4+4
ans = pow(A, pow(B, C))
print(ans % 10)
