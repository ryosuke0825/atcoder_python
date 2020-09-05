import math

N, A, B, C, D = map(int, input().split())

print(min(B*(math.ceil(N/A)), D*(math.ceil(N/C))))
