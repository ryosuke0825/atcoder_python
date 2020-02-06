n = int(input())
sl = ["" for _ in range(n)]
for i in range(n):
    sl[i] = input()

m = int(input())
tl = ["" for _ in range(m)]
for i in range(m):
    tl[i] = input()

ans = 0
for blue_word in sl:
    ans = max(ans, (sl.count(blue_word)-tl.count(blue_word)))

print(ans)
