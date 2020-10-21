X, Y, A, B = map(int, input().split())

ans = 0
while True:
    if X*A < B and X*A < Y:
        X *= A
        ans += 1
    else:
        break

ans += (Y-X-1)//B
print(ans)
