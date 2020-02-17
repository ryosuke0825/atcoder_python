n, m = map(int, input().split())
if n >= 12:
    n = n-12
n = n*30+m*0.5
m *= 6

print(min(abs(n-m), 360-abs(n-m)))
