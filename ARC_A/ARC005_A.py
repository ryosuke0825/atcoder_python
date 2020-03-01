n = int(input())
W = input().split()
t = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']

ans = 0
for w in W:
    w = w.replace('.', '')
    if w in t:
        ans += 1
print(ans)
