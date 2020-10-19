from pprint import pprint

H, W = map(int, input().split())

S = []
S.append(list('#'*(W+2)))
for h in range(H):
    tmp = input()
    tmp = '#'+tmp+'#'
    S.append(list(tmp))
S.append(list('#'*(W+2)))

ans = 0
for h in range(1, H+1):
    for w in range(1, W+1):
        if S[h][w] == '#':
            continue

        if S[h][w+1] == '.':
            ans += 1
        if S[h][w-1] == '.':
            ans += 1
        if S[h+1][w] == '.':
            ans += 1
        if S[h-1][w] == '.':
            ans += 1
print(ans//2)
