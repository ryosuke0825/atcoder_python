a, b, c = map(int, input().split())
abc_len = [a, b, c]
if abc_len.count(5) == 2 and abc_len.count(7) == 1:
    print("YES")
else:
    print("NO")
