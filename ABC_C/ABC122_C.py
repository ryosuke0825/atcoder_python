# TLEエラー
# N, Q = map(int, input().split())
# S = input()
# lr = []
# for _ in range(0, Q):
#     tmp_lr = list(map(int, input().split()))
#     lr.append(tmp_lr)

# for tmp_lr in lr:
#     print(S[tmp_lr[0]-1:tmp_lr[1]].count("AC"))

N, Q = map(int, input().split())
S = input()
t = [0]*(N+1)
for i in range(N):
    t[i+1] = t[i] + (1 if S[i-1:i+1] == "AC" else 0)

lr = []
for i in range(Q):
    tmp_lr = list(map(int, input().split()))
    lr.append(tmp_lr)

for l, r in lr:
    print(t[r]-t[l])
