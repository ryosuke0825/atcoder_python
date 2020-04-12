import copy

N = int(input())
S = input()

RL = [0]*(N+1)
GL = copy.deepcopy(RL)
BL = copy.deepcopy(RL)
R = []
G = []
B = []
for i in range(N):
    if S[i] == 'R':
        R.append(i+1)
        RL[i+1] = 1
    elif S[i] == 'G':
        G.append(i+1)
        GL[i+1] = 1
    elif S[i] == 'B':
        B.append(i+1)
        BL[i+1] = 1

len_r = len(R)
len_g = len(G)
len_b = len(B)
ans = 0
if max(len_r, len_g, len_b) == len_b:
    for i in range(len_r):
        for j in range(len_g):
            ans += len_b
            tmp_abs = abs(R[i]-G[j])

            index = (min(R[i], G[j])-tmp_abs)
            if index > 0 and BL[index] == 1:
                ans -= 1

            index = (max(R[i], G[j])+tmp_abs)
            if index <= N and BL[index] == 1:
                ans -= 1

            if tmp_abs % 2 == 0 and BL[max(R[i], G[j])-(tmp_abs//2)] == 1:
                ans -= 1

elif max(len_r, len_g, len_b) == len_g:
    for i in range(len_r):
        for j in range(len_b):
            ans += len_g
            tmp_abs = abs(R[i]-B[j])

            index = (min(R[i], B[j])-tmp_abs)
            if index > 0 and GL[index] == 1:
                ans -= 1

            index = (max(R[i], B[j])+tmp_abs)
            if index <= N and GL[index] == 1:
                ans -= 1

            if tmp_abs % 2 == 0 and GL[max(R[i], B[j])-(tmp_abs//2)] == 1:
                ans -= 1

else:
    for i in range(len_g):
        for j in range(len_b):
            ans += len_r
            tmp_abs = abs(G[i]-B[j])

            index = (min(G[i], B[j])-tmp_abs)
            if index > 0 and RL[index] == 1:
                ans -= 1

            index = (max(G[i], B[j])+tmp_abs)
            if index <= N and RL[index] == 1:
                ans -= 1

            if tmp_abs % 2 == 0 and RL[max(G[i], B[j])-(tmp_abs//2)] == 1:
                ans -= 1
print(ans)
