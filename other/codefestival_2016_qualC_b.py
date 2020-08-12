K, T = map(int, input().split())
A = list(map(int, input().split()))

print(max(max(A)-1-(K-max(A)), 0))
