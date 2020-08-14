N = int(input())

oturi = 1000-N
ans = 0

ans += oturi//500
oturi %= 500

ans += oturi//100
oturi %= 100

ans += oturi//50
oturi %= 50

ans += oturi//10
oturi %= 10

ans += oturi//5
oturi %= 5

ans += oturi//1
print(ans)
