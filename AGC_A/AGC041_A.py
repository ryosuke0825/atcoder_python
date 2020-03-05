n, a, b = map(int, input().split())

if abs(a-b) % 2 == 0:
    print(abs(a-b)//2)
else:
    print(min((a-1), (b-1), abs(n-a), abs(n-b))+abs(a-b))
