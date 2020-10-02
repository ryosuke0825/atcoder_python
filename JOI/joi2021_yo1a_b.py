from collections import Counter

N = int(input())
S = list(input())

ac = Counter(S)
ans = ''
if 'J' in ac:
    ans = 'J'*ac['J']

if 'O' in ac:
    ans += 'O'*ac['O']

if 'I' in ac:
    ans += 'I'*ac['I']

print(ans)
