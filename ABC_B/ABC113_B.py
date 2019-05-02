N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans_t = abs(A-(T - (H[0] * 0.006)))
ans_h = 1
for i in range(1, N):
    tmp_t = abs(A-(T - (H[i] * 0.006)))
    if tmp_t < ans_t:
        ans_t = tmp_t
        ans_h = i+1
print(ans_h)
