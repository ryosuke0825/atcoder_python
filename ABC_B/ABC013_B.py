a = int(input())
b = int(input())

ans = abs(a-b)
if a <= b:
    print(min(a+10-b, ans))
else:
    print(min(b+10-a, ans))
