N, A, B = map(int, input().split())
S = input()

r = S[A-1:B:]
print(S[:A-1] + r[::-1] + S[B:])
