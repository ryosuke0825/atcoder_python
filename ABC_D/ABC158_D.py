s = input()
q = int(input())

sl = ['']*(q*2+2)
sl[q] = s
m = q-1
u = q+1
rev = False
for _ in range(q):
    query = input().split()

    if query[0] == '1' and not(rev):
        rev = True
    elif query[0] == '1' and rev:
        rev = False

    elif query[0] == '2' and query[1] == '1' and not(rev):
        sl[m] = query[2]
        m -= 1

    elif query[0] == '2' and query[1] == '1' and rev:
        sl[u] = query[2]
        u += 1

    elif query[0] == '2' and query[1] == '2' and not(rev):
        sl[u] = query[2]
        u += 1

    elif query[0] == '2' and query[1] == '2' and rev:
        sl[m] = query[2]
        m -= 1

if rev:
    sl[q] = s[::-1]
    sl.reverse()
    print(''.join(sl))
else:
    print(''.join(sl))
