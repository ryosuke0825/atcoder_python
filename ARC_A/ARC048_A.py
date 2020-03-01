a, b = map(int, input().split())
if a < b <= 0:
    # -5 -4 -3 -2 -1
    print(abs(a-b))
elif a < 0 < b:
    # -3 -2 -1 1 2 3
    print(-(a)+b-1)
else:
    # 1 2 3 4 5
    print(b-a)
