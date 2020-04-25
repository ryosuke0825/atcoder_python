N = int(input())
S = []
for _ in range(N):
    s = input()
    sr = s[::-1]
    S.append([sr, s])

S.sort()
for i in range(N):
    print(S[i][1])
