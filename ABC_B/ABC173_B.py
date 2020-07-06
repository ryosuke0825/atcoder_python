import collections

N = int(input())
ans = []
for _ in range(N):
    ans.append(input())

c = collections.Counter(ans)

if 'AC' in c:
    print('AC x', c['AC'])
else:
    print('AC x', 0)

if 'WA' in c:
    print('WA x', c['WA'])
else:
    print('WA x', 0)

if 'TLE' in c:
    print('TLE x', c['TLE'])
else:
    print('TLE x', 0)

if 'RE' in c:
    print('RE x', c['RE'])
else:
    print('RE x', 0)
