N = int(input())
W = []
ans = True
for i in range(N):
    tmp = input()
    if tmp in W and i != 0:
        ans = False
    W.append(tmp)

if ans:
    last_word = W[0][-1]
    for i in range(1, N):
        if last_word != W[i][0]:
            ans = False
        last_word = W[i][-1]

print("Yes" if ans else "No")
