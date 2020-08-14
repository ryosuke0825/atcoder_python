N, K = map(int, input().split())

# Kが1回の出る場合
cnt = (N-K)*(K-1)*6

# Kが2回出る場合
cnt += (N-1)*3

# 全てKの場合
cnt += 1

print(cnt/(N*N*N))
