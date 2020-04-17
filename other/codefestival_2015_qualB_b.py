import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))

AC = collections.Counter(A)
AC_sort = sorted(AC.items(), key=lambda x: -x[1])

if AC_sort[0][1] > (N/2) and (len(AC_sort) == 1 or (len(AC_sort) >= 2 and AC_sort[0][1] > AC_sort[1][1])):
    print(AC_sort[0][0])
else:
    print('?')
