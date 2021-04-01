N = int(input())

nn = int(N**0.5)+1
ans = {}
for i in range(2, nn):
    for j in range(2, N):
        tmp = i**j
        if tmp > N:
            break

        if not(tmp in ans):
            ans[tmp] = 1
print(N-len(ans))
