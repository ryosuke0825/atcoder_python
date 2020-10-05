N = int(input())
S = input()

w = S.count('.')
b = 0
ans = w
for i in range(N):
    if S[i] == '#':
        b += 1
    else:
        w -= 1
    ans = min(w+b, ans)
print(ans)
