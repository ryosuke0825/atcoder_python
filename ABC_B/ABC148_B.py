N = int(input())
S, T = input().split()

ret = ""
for i in range(0, N):
    ret += S[i]
    ret += T[i]
print(ret)
