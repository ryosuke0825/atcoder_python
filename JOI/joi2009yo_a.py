A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

t = (A[3]*3600+A[4]*60+A[5])-(A[0]*3600+A[1]*60+A[2])
h, t = divmod(t, 3600)
m, s = divmod(t, 60)
print(h, m, s)

t = (B[3]*3600+B[4]*60+B[5])-(B[0]*3600+B[1]*60+B[2])
h, t = divmod(t, 3600)
m, s = divmod(t, 60)
print(h, m, s)

t = (C[3]*3600+C[4]*60+C[5])-(C[0]*3600+C[1]*60+C[2])
h, t = divmod(t, 3600)
m, s = divmod(t, 60)
print(h, m, s)
