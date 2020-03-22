n, a, b = map(int, input().split())
if a % 2 == b % 2:
    print(abs(a-b)//2)
else:
    print(min(a-1, n-b)+1+((b-a)//2))
