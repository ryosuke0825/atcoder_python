n = int(input())

ans = []
for _ in range(n):
    s = input()
    if len(s) == 9 and s.count('i') == 1 and s.count('n') == 2 and s.count('d') == 2 and s.count('e') == 2 and s.count('o') == 1 and s.count('w') == 1:
        ans.append('YES')
    else:
        ans.append('NO')

for a in ans:
    print(a)
