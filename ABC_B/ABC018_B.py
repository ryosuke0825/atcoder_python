s = input()
n = int(input())
for _ in range(n):
    l, r = map(int, input().split())

    lstr = s[:l-1]
    mstr = s[l-1:r]
    mstr = mstr[::-1]
    rstr = s[r:]

    s = lstr + mstr + rstr

print(s)
