N, M = map(int, input().split())
H = list(map(int, input().split()))
A_to_B = [0]*N
for _ in range(M):
    tmp = list(map(int, input().split()))
    if A_to_B[tmp[0]-1] < H[tmp[1]-1]:
        A_to_B[tmp[0]-1] = H[tmp[1]-1]

    if A_to_B[tmp[1]-1] < H[tmp[0]-1]:
        A_to_B[tmp[1]-1] = H[tmp[0]-1]

ans = 0
for i in range(N):
    if H[i] > A_to_B[i]:
        ans += 1
print(ans)
